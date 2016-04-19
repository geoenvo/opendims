from django.contrib import admin
from django.db import models
from django import forms
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
from django.contrib.flatpages.models import FlatPage
from django.core.exceptions import ImproperlyConfigured

try:
    from djgeojson.fields import GeoJSONField
except ImportError:
    GeoJSONField = type(object)
try:
    from django.contrib.gis.db.models import GeometryField
except (ImportError, ImproperlyConfigured):
    # When GEOS is not installed
    GeometryField = type(object)

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from leaflet.forms.widgets import LeafletWidget


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = FlatPage
        fields = ['id', 'title', 'content']


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


"""
Replaced by using django-related-admin
(https://pypi.python.org/pypi/django-related-admin)
"""


def getter_for_related_field(
                             name,
                             admin_order_field=None,
                             short_description=None):
    """
        Create a function that can be attached to a ModelAdmin to use as a
        list_display field, e.g:
        client__name = getter_for_related_field(
            'client__name',
            short_description='Client'
        )
    """
    related_names = name.split('__')

    def getter(self, obj):
        for related_name in related_names:
            obj = getattr(obj, related_name)
        return obj
    getter.admin_order_field = admin_order_field or name
    getter.short_description = (
        short_description or related_names[-1].title().replace('_', ' ')
    )
    return getter


class RelatedFieldAdminMetaclass(type(admin.ModelAdmin)):
    """
        Metaclass used by RelatedFieldAdmin to handle fetching of related
        field values. We have to do this as a metaclass because Django checks
        that list_display fields are supported by the class.
    """
    def __new__(cls, name, bases, attrs):
        new_class = super(RelatedFieldAdminMetaclass, cls).__new__(
            cls, name, bases, attrs
        )

        for field in new_class.list_display:
            if '__' in field:
                setattr(new_class, field, getter_for_related_field(field))

        return new_class


class RelatedFieldAdmin(admin.ModelAdmin):
    """
        Version of ModelAdmin that can use related fields in list_display,
        e.g.:
        list_display = ('address__city', 'address__country__country_code')
    """
    __metaclass__ = RelatedFieldAdminMetaclass

    def get_queryset(self, request):
        qs = super(RelatedFieldAdmin, self).get_queryset(request)

        # include all related fields in queryset
        select_related = [
            field.rsplit('__', 1)[0] for field in self.list_display
            if '__' in field
        ]

        """
        Include all foreign key fields in queryset.
        This is based on ChangeList.get_query_set().
        We have to duplicate it here because select_related() only works once.
        Can't just use list_select_related because we might have
        multiple__depth__fields it won't follow.
        """
        model = qs.model
        for field_name in self.list_display:
            try:
                field = model._meta.get_field(field_name)
            except models.FieldDoesNotExist:
                continue
            if isinstance(field.rel, models.ManyToOneRel):
                select_related.append(field_name)

        return qs.select_related(*select_related)


class LeafletGeoAdminMixin(object):
    """
    Fix required to allow inline leaflet maps in admin.
    Upstream issue: https://github.com/makinacorpus/django-leaflet/issues/60
    """
    widget = LeafletWidget
    map_template = 'leaflet/admin/widget.html'
    modifiable = True
    map_width = '100%'
    map_height = '400px'
    display_raw = False
    settings_overrides = {}

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Overloaded from ModelAdmin to set Leaflet widget
        in form field init params.
        """
        is_geometry = isinstance(db_field, (GeometryField, GeoJSONField))
        is_editable = is_geometry and (db_field.dim < 3 or
                                       self.widget.supports_3d)

        if is_editable:
            kwargs.pop('request', None)  # unsupported for form field
            # Setting the widget with the newly defined widget.
            kwargs['widget'] = self._get_map_widget(db_field)
            return db_field.formfield(**kwargs)
        else:
            return super(LeafletGeoAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)

    def _get_map_widget(self, db_field):
        """
        Overriden LeafletWidget with LeafletGeoAdmin params.
        """
        class LeafletMap(self.widget):
            template_name = self.map_template
            include_media = True
            geom_type = db_field.geom_type
            modifiable = self.modifiable
            map_width = self.map_width
            map_height = self.map_height
            display_raw = self.display_raw
            settings_overrides = self.settings_overrides
        return LeafletMap
