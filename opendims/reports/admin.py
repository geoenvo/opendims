from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

import django
from django.utils.encoding import force_text
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages

from import_export import resources, fields, widgets, forms
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from geolevels.models import Province, City, Subdistrict, Village, RW, RT
from .models import Source, Disaster, Event, Report
from .forms import EventForm


verbose_set_active = _('Set Event as Active')
verbose_set_inactive = _('Set Event as Inactive')
verbose_set_unverified = _('Set Event as Unverified')
verbose_set_verified = _('Set Event as Verified')


def set_unverified(modeladmin, request, queryset):
    queryset.update(status='UNVERIFIED')

set_unverified.short_description = verbose_set_unverified


def set_verified(modeladmin, request, queryset):
    queryset.update(status='VERIFIED')

set_verified.short_description = verbose_set_verified


def set_inactive(modeladmin, request, queryset):
    queryset.update(status='INACTIVE')

set_inactive.short_description = verbose_set_inactive


def set_active(modeladmin, request, queryset):
    queryset.update(status='ACTIVE')

set_active.short_description = verbose_set_active


class ReportInline(admin.TabularInline):
    model = Report
    extra = 3


class SourceAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class DisasterAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class EventResource(resources.ModelResource):
    province = fields.Field(
        column_name='province',
        attribute='province',
        widget=widgets.ForeignKeyWidget(Province, 'name')
    )
    city = fields.Field(
        column_name='city',
        attribute='city',
        widget=widgets.ForeignKeyWidget(City, 'name')
    )
    subdistrict = fields.Field(
        column_name='subdistrict',
        attribute='subdistrict',
        widget=widgets.ForeignKeyWidget(Subdistrict, 'name')
    )
    village = fields.Field(
        column_name='village',
        attribute='village',
        widget=widgets.ForeignKeyWidget(Village, 'name')
    )
    rw = fields.Field(
        column_name='rw',
        attribute='rw',
        widget=widgets.ForeignKeyWidget(RW, 'name')
    )
    rt = fields.Field(
        column_name='rt',
        attribute='rt',
        widget=widgets.ForeignKeyWidget(RT, 'name')
    )

    def before_import(self, dataset, dry_run, **kwargs):
        """Overrides Django-Import-Export method.
        It is necessary to modify the tablib dataset before the real import
        process, to translate from a human friendly input format like this:
        id|disaster|province|city|subdistrict|village|rw |rt|height
        --|--------|--------|----|-----------|-------|---|--|
          |BJR     |        |    |           |ANCOL  |005|  |
          |BJR     |        |    |           |ANCOL  |001|  |
        then in order to match the Event model definition, query the Village-RW
        and RW-RT relation to produce to this:
        id|disaster|province|city|subdistrict|village|rw              |rt|height
        --|--------|--------|----|-----------|-------|----------------|--|
          |BJR     |        |    |           |ANCOL  |3175020003005000|  |
          |BJR     |        |    |           |ANCOL  |3175020003001000|  |
        Also checks whether the row's Geolevels relation is valid, if not
        the row is not imported.
        """
        # print 'DEBUG BEFORE'
        # print dataset

        # Get request object for sending error messages
        request = kwargs.pop('request', None)
        i = 0
        row_count = i + 2
        last = dataset.height - 1
        while i <= last:
            # Get the top row
            row = dataset[0]
            """
            Get the row contents, by default named Geolevels are uppercase
            in the database
            """
            id = row[0]
            disaster = row[1].upper()
            province = row[2].upper()
            city = row[3].upper()
            subdistrict = row[4].upper()
            village = row[5].upper()
            rw = row[6]
            rt = row[7]
            # Pad single digit RT/RW with zeros
            if rw and len(rw) < 3:
                diff = 3 - len(rw)
                for i in range(diff):
                    rw = '0' + rw
            if rt and len(rt) < 3:
                diff = 3 - len(rt)
                for i in range(diff):
                    rt = '0' + rt
            height = row[8]
            # Validate Geolevels relations
            valid_geolevels = True
            if rw and not village:
                valid_geolevels = False
            if rt and not rw:
                valid_geolevels = False
            if province and valid_geolevels:
                try:
                    Province.objects.get(name=province)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Province not found. Skipping this row for import.')))
            if city and province and valid_geolevels:
                try:
                    City.objects.get(name=city, province__name=province)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('City not found. Skipping this row for import.')))
            if subdistrict and city and valid_geolevels:
                try:
                    Subdistrict.objects.get(name=subdistrict, city__name=city)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Subdistrict not found. Skipping this row for import.')))
            if village and subdistrict and valid_geolevels:
                try:
                    Village.objects.get(
                        name=village,
                        subdistrict__name=subdistrict
                    )
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('Village not found. Skipping this row for import.')))
            if rw and village and valid_geolevels:
                try:
                    rw_instance = RW.objects.get(name=rw, village__name=village)
                    rw = unicode(rw_instance.pk)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('RW not found. Skipping this row for import.')))
            if rt and rw and valid_geolevels:
                try:
                    rt_instance = RT.objects.get(name=rt, rw=rw_instance)
                    rt = unicode(rt_instance.pk)
                except ObjectDoesNotExist:
                    valid_geolevels = False
                    messages.error(request, "Error (row {}): {}".format(row_count, _('RT not found. Skipping this row for import.')))
            new_row = (
                id,
                disaster,
                province,
                city,
                subdistrict,
                village,
                rw,
                rt,
                height
            )
            """
            If relations are invalid don't push row to the dataset so it
            doesn't get imported
            """
            if valid_geolevels:
                dataset.rpush(new_row)
            dataset.lpop()
            i = i + 1
            row_count = i + 2
        # print 'DEBUG AFTER'
        # print dataset
        for field in self.get_fields():
            # print field.attribute, field.column_name, field.widget
            """
            Since the dataset now contains the PK of RW/RT, update the
            ForeignKeyWidget to query for PK instead of name column.
            """
            if field.attribute == 'rw' or field.attribute == 'rt':
                # print field.widget.model, field.widget.field
                # print field.widget.field
                field.widget.field = 'pk'

    class Meta:
        model = Event
        fields = (
            'id',
            'disaster',
            'province',
            'city',
            'subdistrict',
            'village',
            'rw',
            'rt',
            'height'
        )
        export_order = fields


verbose_event_details = _('Event details')
verbose_affected_area = _('Affected area')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')


class EventAdmin(ImportExportModelAdmin,
                 ExportActionModelAdmin,
                 LeafletGeoAdmin):
    resource_class = EventResource

    # Leaflet widget override
    settings_overrides = {
        'DEFAULT_ZOOM': 11,
    }

    fieldsets = [
        (verbose_event_details, {
            'fields': [
                'created',
                'disaster',
                'status',
                'height',
                'magnitude',
                'note'
            ]
        }),
        (verbose_affected_area, {
            'fields': [
                'province',
                'city',
                'subdistrict',
                'village',
                'rw',
                'rt',
                'point'
            ]
        }),
    ]
    list_display = [
        'created',
        'updated',
        'status',
        'disaster',
        'province_admin_url',
        'city_admin_url',
        'subdistrict_admin_url',
        'village_admin_url',
        'rw_admin_url',
        'rt_admin_url',
        'height',
        'magnitude',
        'note'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['created', 'updated', 'status', 'disaster']
    search_fields = [
        'province__name',
        'city__name',
        'subdistrict__name',
        'village__name',
        'note'
    ]
    actions = [set_active, set_inactive]
    inlines = [ReportInline]
    form = EventForm

    def import_action(self, request, *args, **kwargs):
        '''
        Overrides import_action() in import_export/admin.py
        just to pass a request object to import_data() to
        be used in before_import().
        '''
        resource = self.get_import_resource_class()()

        context = {}

        import_formats = self.get_import_formats()
        form = forms.ImportForm(import_formats,
                                request.POST or None,
                                request.FILES or None)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
            import_file = form.cleaned_data['import_file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            tmp_storage = self.get_tmp_storage_class()()
            data = bytes()
            for chunk in import_file.chunks():
                data += chunk

            tmp_storage.save(data, input_format.get_read_mode())

            # then read the file, using the proper format-specific mode
            # warning, big files may exceed memory
            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_text(data, self.from_encoding)
                dataset = input_format.create_dataset(data)
            except UnicodeDecodeError as e:
                return HttpResponse(_(u"<h1>Imported file is not in unicode: %s</h1>" % e))
            except Exception as e:
                return HttpResponse(_(u"<h1>%s encountred while trying to read file: %s</h1>" % (type(e).__name__, e)))
            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=False,
                                          file_name=import_file.name,
                                          user=request.user, request=request)

            context['result'] = result

            if not result.has_errors():
                context['confirm_form'] = forms.ConfirmImportForm(initial={
                    'import_file_name': tmp_storage.name,
                    'original_file_name': import_file.name,
                    'input_format': form.cleaned_data['input_format'],
                })

        if django.VERSION >= (1, 8, 0):
            context.update(self.admin_site.each_context(request))
        elif django.VERSION >= (1, 7, 0):
            context.update(self.admin_site.each_context())

        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_fields()]

        return TemplateResponse(request, [self.import_template_name],
                                context)

    def province_admin_url(self, obj):
        if not obj.province:
            return '-'
        return format_html(
            "<a href='{url}'>{province}</a>",
            url=obj.province.get_admin_url(),
            province=obj.province
        )

    province_admin_url.short_description = verbose_province

    def city_admin_url(self, obj):
        if not obj.city:
            return '-'
        return format_html(
            "<a href='{url}'>{city}</a>",
            url=obj.city.get_admin_url(),
            city=obj.city
        )

    city_admin_url.short_description = verbose_city

    def subdistrict_admin_url(self, obj):
        if not obj.subdistrict:
            return '-'
        return format_html(
            "<a href='{url}'>{subdistrict}</a>",
            url=obj.subdistrict.get_admin_url(),
            subdistrict=obj.subdistrict
        )

    subdistrict_admin_url.short_description = verbose_subdistrict

    def village_admin_url(self, obj):
        if not obj.village:
            return '-'
        return format_html(
            "<a href='{url}'>{village}</a>",
            url=obj.village.get_admin_url(),
            village=obj.village
        )

    village_admin_url.short_description = verbose_village

    def rw_admin_url(self, obj):
        if not obj.rw:
            return '-'
        return format_html(
            "<a href='{url}'>{rw}</a>",
            url=obj.rw.get_admin_url(),
            rw=obj.rw
        )

    rw_admin_url.short_description = verbose_rw

    def rt_admin_url(self, obj):
        if not obj.rt:
            return '-'
        return format_html(
            "<a href='{url}'>{rt}</a>",
            url=obj.rt.get_admin_url(),
            rt=obj.rt
        )

    rt_admin_url.short_description = verbose_rt


verbose_report_details = _('Report details')
verbose_event = _('Event')


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_report_details, {
            'fields': [
                'created',
                'updated',
                'event',
                'source',
                'status',
                'note'
            ]
        })
    ]
    list_display = [
        'created',
        'updated',
        'event_admin_url',
        'source',
        'status',
        'note'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['created', 'updated', 'source', 'status']
    search_fields = ['note']
    actions = [set_verified, set_unverified]

    def event_admin_url(self, obj):
        if not obj.event:
            return '-'
        return format_html(
            "<a href='{url}'>{event}</a>",
            url=obj.event.get_admin_url(),
            event=obj.event
        )

    event_admin_url.short_description = verbose_event


admin.site.register(Source, SourceAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Event, EventAdmin)
