from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import Activity, Location
from common.serializers import DateTimeFieldTZ


class ActivitySerializer(serializers.ModelSerializer):
    agency_name = serializers.SerializerMethodField()
    created = DateTimeFieldTZ()
    updated = DateTimeFieldTZ()

    def get_agency_name(self, obj):
        if obj.agency:
            return obj.agency.name

    class Meta:
        model = Activity
        field = (
            'id',
            'created',
            'updated',
            'event',
            'name',
            'type',
            'start',
            'end',
            'agency',
            'agency_name',
            'funding',
            'status',
            'year'
        )


class ActivityLocationSerializer(gis_serializers.GeoFeatureModelSerializer):
    activity = serializers.SerializerMethodField()
    geometry = gis_serializers.GeometrySerializerMethodField()
    province_name = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    subdistrict_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()
    rw_name = serializers.SerializerMethodField()
    rt_name = serializers.SerializerMethodField()

    def get_activity(self, obj):
        activity = obj.activity
        serializer = ActivitySerializer(instance=activity)
        return serializer.data

    def get_province_name(self, obj):
        if obj.province:
            return obj.province.name

    def get_city_name(self, obj):
        if obj.city:
            return obj.city.name

    def get_subdistrict_name(self, obj):
        if obj.subdistrict:
            return obj.subdistrict.name

    def get_village_name(self, obj):
        if obj.village:
            return obj.village.name

    def get_rw_name(self, obj):
        if obj.rw:
            return obj.rw.name

    def get_rt_name(self, obj):
        if obj.rt:
            return obj.rt.name

    def get_geometry(self, obj):
        """
        Return the Location polygon of the lowest available Geolevel.
        """
        if obj.rt:
            return obj.rt.polygon
        elif obj.rw:
            return obj.rw.polygon
        elif obj.village:
            return obj.village.polygon
        elif obj.subdistrict:
            return obj.subdistrict.polygon
        elif obj.city:
            return obj.city.polygon
        elif obj.province:
            return obj.province.polygon
        else:
            return None

    class Meta:
        model = Location
        geo_field = 'geometry'
        fields = (
            'id',
            'province',
            'province_name',
            'city',
            'city_name',
            'subdistrict',
            'subdistrict_name',
            'village',
            'village_name',
            'rw',
            'rw_name',
            'rt',
            'rt_name',
            'activity'
        )
