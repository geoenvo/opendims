import datetime

from django.utils import timezone

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from .models import SensorStation, SensorReport
from common.serializers import DateTimeFieldTZ


class SensorReportSerializer(serializers.ModelSerializer):
    created = DateTimeFieldTZ()
    updated = DateTimeFieldTZ()

    class Meta:
        model = SensorReport
        fields = (
            'id',
            'created',
            'updated',
            'temperature',
            'humidity',
            'pressure',
            'wind_speed',
            'wind_direction',
            'day_rain',
            'rain_rate',
            'uv_index',
            'solar_radiation',

        )


class SensorSerializer(gis_serializers.GeoFeatureModelSerializer):
    reports = serializers.SerializerMethodField()

    def get_reports(self, obj):
        """
        If date parameter is not provided, Return sensor station reports
        from the current day only.
        """
        reports = SensorReport.objects.filter(sensorstation=obj).order_by('-created')
        date = self.context['request'].GET.get('date', None)
        if date:
            try:
                date = timezone.make_aware(datetime.datetime.strptime(date, '%Y-%m-%d'))
                reports = reports.filter(
                    created__date=date.date()
                )
            except ValueError:
                return SensorReport.objects.none()
        else:
            now = timezone.localtime(timezone.now())
            reports = reports.filter(
                created__date=now.date()
            )
        serializer = SensorReportSerializer(instance=reports, many=True)
        return serializer.data

    class Meta:
        model = SensorStation
        geo_field = 'point'
        fields = (
            'id',
            'name',
            'note',
            'reports',
        )
