from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import ReportAutoSummary
from common.serializers import DateTimeFieldTZ

class JaksafeSerializer(gis_serializers.GeoFeatureModelSerializer):
    created = DateTimeFieldTZ()
    geometry = gis_serializers.GeometrySerializerMethodField()
    village_name = serializers.SerializerMethodField()

    def get_geometry(self, obj):
        return obj.village.polygon
    def get_village_name(self, obj):
        return obj.village.name

    class Meta:
        model = ReportAutoSummary
        geo_field = 'geometry'
        fields = (
            'id',
            'created',
            'village',
            'village_name',
            'rw',
            'source',
            'note',
            'damage_infrastruktur',
            'loss_infrastruktur',
            'damage_lintas_sektor',
            'loss_lintas_sektor',
            'damage_produktif',
            'loss_produktif',
            'damage_sosial_perumahan',
            'loss_sosial_perumahan',
            'damage_total',
            'loss_total',
        )
