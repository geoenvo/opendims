from rest_framework import serializers

from .models import Event, Report

from rest_framework_gis.serializers import GeoFeatureModelSerializer

from geolevels.models import RW


class RWSerializers(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = RW
        geo_field = 'polygon'
        id_fields = False

        fields = ()


class EventSerializers(GeoFeatureModelSerializer):
    rw = RWSerializers()

    class Meta:
        model = Event
        geo_field = 'point'
        fields = ('id', 'disaster', 'point', 'created', 'updated', 'status', 'note', 'height', 'magnitude', 'province', 'city', 'subdistrict', 'village', 'rw', 'rt',)


class ReportSerializers(serializers.ModelSerializer):
        event = EventSerializers()

        class Meta:
                model = Report
                field = ('event',
                         'source',
                         'created',
                         'updated',
                         'status',
                         'note')
