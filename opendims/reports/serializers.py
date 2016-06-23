from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import Event, Report
from common.serializers import DateTimeFieldTZ


class ReportSerializer(serializers.ModelSerializer):
    source_note = serializers.SerializerMethodField()
    created = DateTimeFieldTZ()
    updated = DateTimeFieldTZ()

    def get_source_note(self, obj):
        return obj.source.note

    class Meta:
        model = Report
        field = (
            'id',
            'event',
            'source',
            'source_note',
            'created',
            'updated',
            'status',
            'note'
        )


class EventSerializer(gis_serializers.GeoFeatureModelSerializer):
    reports = serializers.SerializerMethodField()
    geometry = gis_serializers.GeometrySerializerMethodField()
    disaster_note = serializers.SerializerMethodField()
    created = DateTimeFieldTZ()
    updated = DateTimeFieldTZ()
    closed = DateTimeFieldTZ()
    province_name = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    subdistrict_name = serializers.SerializerMethodField()
    village_name = serializers.SerializerMethodField()
    rw_name = serializers.SerializerMethodField()
    rt_name = serializers.SerializerMethodField()

    def get_reports(self, obj):
        reports = Report.objects.filter(event=obj).order_by('-created')
        serializer = ReportSerializer(instance=reports, many=True)
        return serializer.data

    def get_disaster_note(self, obj):
        return obj.disaster.note

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
            'disaster_note',
            'created',
            'updated',
            'status',
            'closed',
            'note',
            'height_min',
            'height',
            'magnitude',
            'depth',
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
            'point',
            'reports',
        )
