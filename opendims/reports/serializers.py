from rest_framework import serializers

from geolevels.models import Province, City, Subdistrict, Village, RW, RT
from .models import Source, Disaster, Event, Report

class EventSerializers(serializers.ModelSerializer):
        class Meta:
                model= Event
                field = ('id',
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
                         'rw', 'rt')

class ReportSerializers(serializers.ModelSerializer):
        event = EventSerializers()
        class Meta:
                model= Report
                field = ('event',
                         'source',
                         'created',
                         'updated',
                         'status',
                         'note')
