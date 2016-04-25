from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import AWSStation, AWSReport
verbose_awsstation_details = _('AWS Station details')
verbose_awsreport_details = _('AWS Report details')


class AWSStationAdmin(LeafletGeoAdmin):
    settings_overrides = {
            'DEFAULT_ZOOM': 13,
        }

    fieldsets = [
        (verbose_awsstation_details, {
            'fields': [
                'name',
                'point',
                'note'
            ]
        })
    ]
    list_display = [
        'name'
    ]


class AWSReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_awsreport_details, {
            'fields': [
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
            ]
        })
    ]
    list_display = [
        'created',
        'updated',
        'awsstation',
        'temperature',
        'pressure',
        'wind_speed',
        'wind_direction',
        'day_rain',
        'rain_rate',
        'uv_index',
        'solar_radiation'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['awsstation', 'temperature']
    search_fields = ['awsstation']


admin.site.register(AWSStation, AWSStationAdmin)
admin.site.register(AWSReport, AWSReportAdmin)
