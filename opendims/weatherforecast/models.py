from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from geolevels.models import City, Province
from common.models import CommonAbstractModel


verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_note = _('Note')
verbose_forecastmorning = _('Morning forecast')
verbose_forecastnoon = _('Noon forecast')
verbose_forecastnight = _('Night forecast')
verbose_forecast = _('Forecast')
verbose_city = _('City')
verbose_province = _('Province')
verbose_tempmin = _('Temperature min')
verbose_tempmax = _('Temperature max')
verbose_humidmin = _('Humidity min')
verbose_humidmax = _('Humidity max')


class WeatherForecastReport(CommonAbstractModel):
    FORECAST_CHOICES = (
        ('CERAH', _('Clear')),
        ('CERAH BERAWAN', _('Partly cloudy')),
        ('BERAWAN', _('Cloudy')),
        ('HUJAN RINGAN', _('Light rain')),
        ('HUJAN SEDANG', _('Moderate rain')),
        ('HUJAN LEBAT', _('Heavy rain')),
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    forecast_morning = models.CharField(
        max_length=50,
        choices=FORECAST_CHOICES,
        blank=True,
        verbose_name=verbose_forecastmorning
    )
    forecast_noon = models.CharField(
        max_length=50,
        choices=FORECAST_CHOICES,
        blank=True,
        verbose_name=verbose_forecastnoon
    )
    forecast_night = models.CharField(
        max_length=50,
        choices=FORECAST_CHOICES,
        blank=True,
        verbose_name=verbose_forecastnight
    )
    forecast = models.CharField(
        max_length=50,
        choices=FORECAST_CHOICES,
        blank=True,
        verbose_name=verbose_forecast
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        verbose_name=verbose_city
    )
    province = models.ForeignKey(
        Province,
        null=True,
        blank=True,
        verbose_name=verbose_province
    )
    temperature_min = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        verbose_name=verbose_tempmin
    )
    temperature_max = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        verbose_name=verbose_tempmax
    )
    humidity_min = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_humidmin
    )
    humidity_max = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_humidmax
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.province, self.city, timezone.localtime(self.created))
