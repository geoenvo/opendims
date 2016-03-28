from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import Event, Report

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        field = ('id', 'source', 'created', 'updated', 'status', 'note')


class EventSerializer(gis_serializers.GeoFeatureModelSerializer):
    reports = ReportSerializer(many=True, read_only=True)
    geometry = gis_serializers.GeometrySerializerMethodField()
    province_name = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    subdistrict_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()
    rw_name = serializers.SerializerMethodField()

    def get_rw_name(self, obj):
        return obj.rw.name

    def get_village_name(self, obj):
        return obj.village.name

    def get_subdistrict_name(self, obj):
        return obj.subdistrict.name

    def get_city_name(self, obj):
        return obj.city.name

    def get_province_name(self, obj):
        return obj.province.name

    def get_geometry(self, obj):
        """
        Return the Event point, or polygon of the lowest available Geolevel.
        """
        if obj.point:
            return obj.point
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
        model = Event
        geo_field = 'geometry'
        fields = (
            'id',
            'disaster',
            'point',
            'created',
            'updated',
            'status',
            'note',
            'height',
            'magnitude',
            'province_name',
            'province',
            'city_name',
            'city',
            'subdistrict_name',
            'subdistrict',
            'village_name',
            'village',
            'rw_name',
            'rw',
            'rt',
            'reports',
        )
