from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import AWSStation, AWSReport


class AWSStationAdmin(LeafletGeoAdmin):
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


class AWSReportAdmin(admin.ModelAdmin):
    fields = (
        'created',
        'awsstation',
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
        'awsstation'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['awsstation', 'created']
    search_fields = ['awsstation']


admin.site.register(AWSStation, AWSStationAdmin)
admin.site.register(AWSReport, AWSReportAdmin)
