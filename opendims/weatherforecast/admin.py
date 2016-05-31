from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import WeatherForecastReport


class WeatherForecastReportAdmin(admin.ModelAdmin):
    fields = (
        'created',
        'province',
        'city',
        'forecast',
        ('forecast_morning', 'forecast_noon', 'forecast_night'),
        ('temperature_min', 'temperature_max'),
        ('humidity_min', 'humidity_max'),
        'note'
    )
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
    date_hierarchy = 'created'
    list_filter = ['city', 'forecast_morning', 'forecast_noon', 'forecast_night', 'updated']
    search_fields = ['note']

admin.site.register(WeatherForecastReport, WeatherForecastReportAdmin)
