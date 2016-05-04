from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from geolevels.models import City, Province
from django.core.urlresolvers import reverse

from common.models import CommonAbstractModel

verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_note = _('Note')
verbose_forecastmorning = _('Morning Forecast')
verbose_forecastnoon = _('Noon Forecast')
verbose_forecastnight = _('Night Forecast')
verbose_forecast = _('Forecast')
verbose_city = _('City')
verbose_province = _('Province')
verbose_tempmin = _('Temperature Min')
verbose_tempmax = _('Temperature Max')
verbose_humidmin = _('Humidity Min')
verbose_humidmax = _('Humidity Max')


class WeatherForecastReport(CommonAbstractModel):
    FORECAST_CHOICES = (
        ('CERAH', _('Cerah')),
        ('CERAH BERAWAN', _('Cerah Berawan')),
        ('BERAWAN', _('Berawan')),
        ('HUJAN RINGAN', _('Hujan Ringan')),
        ('HUJAN SEDANG', _('Hujan Sedang')),
        ('HUJAN DERAS', _('Hujan Deras')),
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
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.city, self.province, timezone.localtime(self.created))

    def get_absolute_url(self):
        return reverse('weatherforecast:weatherforecastreport_list')
