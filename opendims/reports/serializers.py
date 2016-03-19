from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import Event, Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        field = ('id', 'source', 'created', 'updated', 'status', 'note')


class EventSerializer(gis_serializers.GeoFeatureModelSerializer):
    reports = ReportSerializer(many=True, read_only=True)
    event_geom = gis_serializers.GeometrySerializerMethodField()

    def get_event_geom(self, obj):
        """
        Return the polygon of the lowest available Geolevel.
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
        model = Event
        geo_field = 'event_geom'
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
            'province',
            'city',
            'subdistrict',
            'village',
            'rw',
            'rt',
            'reports',
        )
