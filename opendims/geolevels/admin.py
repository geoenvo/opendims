from __future__ import unicode_literals

from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from django.db import models

from .models import Province, City, Subdistrict, Village, RW, RT


def getter_for_related_field(name, admin_order_field=None, short_description=None):
    """
        Create a function that can be attached to a ModelAdmin to use as a list_display field, e.g:
        client__name = getter_for_related_field('client__name', short_description='Client')
    """
    related_names = name.split('__')
    def getter(self, obj):
        for related_name in related_names:
            obj = getattr(obj, related_name)
        return obj
    getter.admin_order_field = admin_order_field or name
    getter.short_description = short_description or related_names[-1].title().replace('_', ' ')
    return getter


class RelatedFieldAdminMetaclass(type(admin.ModelAdmin)):
    """
        Metaclass used by RelatedFieldAdmin to handle fetching of related field values.
        We have to do this as a metaclass because Django checks that list_display fields are supported by the class.
    """
    def __new__(cls, name, bases, attrs):
        new_class = super(RelatedFieldAdminMetaclass, cls).__new__(cls, name, bases, attrs)

        for field in new_class.list_display:
            if '__' in field:
                setattr(new_class, field, getter_for_related_field(field))

        return new_class


class RelatedFieldAdmin(LeafletGeoAdmin):
    """
        Version of ModelAdmin that can use related fields in list_display, e.g.:
        list_display = ('address__city', 'address__country__country_code')
    """
    __metaclass__ = RelatedFieldAdminMetaclass
    
    def get_queryset(self, request):
        qs = super(RelatedFieldAdmin, self).get_queryset(request)

        # include all related fields in queryset
        select_related = [field.rsplit('__', 1)[0] for field in self.list_display if '__' in field]

        # Include all foreign key fields in queryset.
        # This is based on ChangeList.get_query_set().
        # We have to duplicate it here because select_related() only works once.
        # Can't just use list_select_related because we might have multiple__depth__fields it won't follow.
        model = qs.model
        for field_name in self.list_display:
            try:
                field = model._meta.get_field(field_name)
            except models.FieldDoesNotExist:
                continue
            if isinstance(field.rel, models.ManyToOneRel):
                select_related.append(field_name)

        return qs.select_related(*select_related)


class ProvinceAdmin(RelatedFieldAdmin):
    list_display = ('id', 'name', 'note')
    search_fields = ['name']


class CityAdmin(RelatedFieldAdmin):
    list_display = ('id', 'sort_province_by_name', 'name', 'note')
    search_fields = ['province__name', 'name']
    
    sort_province_by_name = getter_for_related_field(
        'province',
        admin_order_field='province__name'
    )


class SubdistrictAdmin(RelatedFieldAdmin):
    list_display = ('id', 'sort_province_by_name', 'sort_city_by_name', 'name', 'note')
    search_fields = ['city__province__name', 'city__name', 'name']
    
    sort_province_by_name = getter_for_related_field(
        'city__province',
        admin_order_field='city__province__name'
    )
    
    sort_city_by_name = getter_for_related_field(
        'city',
        admin_order_field='city__name'
    )


class VillageAdmin(RelatedFieldAdmin):
    list_display = (
        'id',
        'sort_province_by_name',
        'sort_city_by_name',
        'sort_subdistrict_by_name',
        'name',
        'note'
    )
    search_fields = [
        'subdistrict__city__province__name',
        'subdistrict__city__name',
        'subdistrict__name'
    ]
    
    sort_province_by_name = getter_for_related_field(
        'subdistrict__city__province',
        admin_order_field='subdistrict__city__province__name'
    )
    
    sort_city_by_name = getter_for_related_field(
        'subdistrict__city',
        admin_order_field='subdistrict__city__name'
    )
    
    sort_subdistrict_by_name = getter_for_related_field(
        'subdistrict',
        admin_order_field='subdistrict__name'
    )


class RWAdmin(RelatedFieldAdmin):
    list_display = (
        'id',
        'sort_province_by_name',
        'sort_city_by_name',
        'sort_subdistrict_by_name',
        'sort_village_by_name',
        'name',
        'note'
    )
    search_fields = [
        'village__subdistrict__city__province__name',
        'village__subdistrict__city__name',
        'village__subdistrict__name',
        'village__name'
    ]
    
    sort_province_by_name = getter_for_related_field(
        'village__subdistrict__city__province',
        admin_order_field='village__subdistrict__city__province__name'
    )
    
    sort_city_by_name = getter_for_related_field(
        'village__subdistrict__city',
        admin_order_field='village__subdistrict__city__name'
    )
    
    sort_subdistrict_by_name = getter_for_related_field(
        'village__subdistrict',
        admin_order_field='village__subdistrict__name'
    )
    
    sort_village_by_name = getter_for_related_field(
        'village',
        admin_order_field='village__name'
    )


class RTAdmin(RelatedFieldAdmin):
    list_display = (
        'id',
        'sort_province_by_name',
        'sort_city_by_name',
        'sort_subdistrict_by_name',
        'sort_village_by_name',
        'rw',
        'name',
        'note'
    )
    search_fields = [
        'rw__village__subdistrict__province__name',
        'rw__village__subdistrict__city__name',
        'rw__village__subdistrict__name',
        'rw__village__name'
    ]  # No use searching RW by name
    
    sort_province_by_name = getter_for_related_field(
        'rw__village__subdistrict__province',
        admin_order_field='rw__village__subdistrict__province__name'
    )
    
    sort_city_by_name = getter_for_related_field(
        'rw__village__subdistrict__city',
        admin_order_field='rw__village__subdistrict__city__name'
    )
    
    sort_subdistrict_by_name = getter_for_related_field(
        'rw__village__subdistrict',
        admin_order_field='rw__village__subdistrict__name'
    )
    
    sort_village_by_name = getter_for_related_field(
        'rw__village',
        admin_order_field='rw__village__name'
    )


admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Subdistrict, SubdistrictAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(RW, RWAdmin)
admin.site.register(RT, RTAdmin)
