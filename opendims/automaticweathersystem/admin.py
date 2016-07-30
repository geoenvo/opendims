from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import SensorStation, SensorReport


class SensorStationAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_ZOOM': 13,
    }
    fields = (
        'name',
        'point',
        'note'
    )
    list_display = [
        'name',
        'note'
    ]


class SensorReportAdmin(admin.ModelAdmin):
    fields = (
        'created',
        'sensorstation',
        'temperature',
        'humidity',
        'pressure',
        'wind_speed',
        'wind_direction',
        'day_rain',
        'rain_rate',
        'uv_index',
        'solar_radiation'
    )
    list_display = [
        'created',
        'updated',
        'sensorstation'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['sensorstation', 'created']
    search_fields = ['sensorstation']


admin.site.register(SensorStation, SensorStationAdmin)
admin.site.register(SensorReport, SensorReportAdmin)
