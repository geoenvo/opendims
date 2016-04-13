from __future__ import unicode_literals
import os, json

from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin
from related_admin import RelatedFieldAdmin, getter_for_related_field

from .models import Province, City, Subdistrict, Village, RW, RT
from .forms import CityForm, SubdistrictForm, VillageForm, RWForm, RTForm


class GeolevelsAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        Replace Geolevel multipolygon with uploaded .geojson CRS84 file.
        Delete the .geojson file after updating the multipolygon.
        """
        obj.save()
        if obj.geojson:
            with open(obj.geojson.path) as f:
                geojson = json.load(f)
                f.close()
                if 'features' in geojson and 'crs' in geojson:
                    crs = geojson['crs']['properties']['name']
                    if 'CRS84' in crs:
                        for feature in geojson['features']:
                            if feature['geometry']['type'] == 'MultiPolygon':
                                geometry = feature['geometry']
                                if geometry:
                                    obj.polygon = json.dumps(geometry)
            try:
                os.remove(obj.geojson.path)
            except:
                pass
            obj.geojson = None
            obj.save()


class ProvinceAdmin(RelatedFieldAdmin, LeafletGeoAdmin, GeolevelsAdmin):
    list_display = ('id', 'name', 'note')
    search_fields = ['name']


class CityAdmin(RelatedFieldAdmin, LeafletGeoAdmin, GeolevelsAdmin):
    list_display = ('id', 'sort_province_by_name', 'name', 'note')
    search_fields = ['province__name', 'name']
    form = CityForm

    sort_province_by_name = getter_for_related_field(
        'province',
        admin_order_field='province__name'
    )


class SubdistrictAdmin(RelatedFieldAdmin, LeafletGeoAdmin, GeolevelsAdmin):
    list_display = (
        'id',
        'sort_province_by_name',
        'sort_city_by_name',
        'name',
        'note'
    )
    search_fields = ['city__province__name', 'city__name', 'name']
    form = SubdistrictForm

    sort_province_by_name = getter_for_related_field(
        'city__province',
        admin_order_field='city__province__name'
    )

    sort_city_by_name = getter_for_related_field(
        'city',
        admin_order_field='city__name'
    )


class VillageAdmin(RelatedFieldAdmin, LeafletGeoAdmin, GeolevelsAdmin):
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
    form = VillageForm

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


class RWAdmin(RelatedFieldAdmin, LeafletGeoAdmin, GeolevelsAdmin):
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
    form = RWForm

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


class RTAdmin(RelatedFieldAdmin, LeafletGeoAdmin, GeolevelsAdmin):
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
    form = RTForm

    sort_province_by_name = getter_for_related_field(
        'rw__village__subdistrict__city__province',
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
