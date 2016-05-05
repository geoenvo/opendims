from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import WeatherForecastReport

verbose_weatherforecasreport_details = _('Weather Forecast Report details')


class WeatherForecastReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_weatherforecasreport_details, {
            'fields': [
                'created',
                'province',
                'city',
                'forecast',
                ('forecast_morning', 'forecast_noon', 'forecast_night'),
                ('temperature_min', 'temperature_max'),
                ('humidity_min', 'humidity_max'),
                'note'
            ]
        })
    ]
    list_display = [
        'created',
        'updated',
        'province',
        'city',
        'forecast_morning',
        'forecast_noon',
        'forecast_night'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['city', 'forecast_morning', 'forecast_noon', 'forecast_night', 'updated']
    search_fields = ['note']

admin.site.register(WeatherForecastReport, WeatherForecastReportAdmin)
