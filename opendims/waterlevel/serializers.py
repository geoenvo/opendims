import datetime

from django.utils import timezone

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import WaterGate, WaterLevelReport
from common.serializers import DateTimeFieldTZ


class WaterLevelReportSerializer(serializers.ModelSerializer):
    created = DateTimeFieldTZ()
    updated = DateTimeFieldTZ()

    class Meta:
        model = WaterLevelReport
        fields = (
            'id',
            'created',
            'updated',
            'height',
            'weather',
        )


class WaterLevelSerializer(gis_serializers.GeoFeatureModelSerializer):
    reports = serializers.SerializerMethodField()

    def get_reports(self, obj):
        reports = WaterLevelReport.objects.filter(watergate=obj).order_by('-created')
        date = self.context['request'].GET.get('date', None)
        if date:
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
                reports = reports.filter(
                    created__year=date.year,
                    created__month=date.month,
                    created__day=date.day
                )
            except ValueError:
                return []
        else:
            # No date parameter, return reports from current day
            now = timezone.localtime(timezone.now())
            reports = reports.filter(
                created__year=now.year,
                created__month=now.month,
                created__day=now.day
            )
        serializer = WaterLevelReportSerializer(instance=reports, many=True)
        return serializer.data

    class Meta:
        model = WaterGate
        geo_field = 'point'
        fields = (
            'id',
            'name',
            'siaga_1_min',
            'siaga_1_max',
            'siaga_2_min',
            'siaga_2_max',
            'siaga_3_min',
            'siaga_3_max',
            'note',
            'reports',
        )
