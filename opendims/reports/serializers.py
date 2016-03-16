from rest_framework import serializers

from .models import Event, Report

from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField


class EventSerializer(GeoFeatureModelSerializer):
    rw_polygon = GeometrySerializerMethodField()

    def get_rw_polygon(self, obj):
        if obj.rw:
            return obj.rw.polygon
        else:
            return None

    class Meta:
        model = Event
        geo_field = 'rw_polygon'
        fields = ('id', 'disaster', 'point', 'created', 'updated', 'status', 'note', 'height', 'magnitude', 'province', 'city', 'subdistrict', 'village', 'rw', 'rt',)


class ReportSerializer(serializers.ModelSerializer):
        event = EventSerializer()

        class Meta:
                model = Report
                field = ('event',
                         'source',
                         'created',
                         'updated',
                         'status',
                         'note')
