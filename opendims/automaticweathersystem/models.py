from __future__ import unicode_literals
from decimal import Decimal

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator

from common.models import CommonAbstractModel


verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_point = _('Point')
verbose_name = _('Name')
verbose_note = _('Note')
verbose_awsstation = _('AWS station')
verbose_temperature = _('Temperature')
verbose_humidity = _('Humidity')
verbose_pressure = _('Pressure')
verbose_windspeed = _('Wind speed')
verbose_winddir = _('Wind direction')
verbose_dayrain = _('Day rain')
verbose_rainrate = _('Rain rate')
verbose_uvindex = _('UV index')
verbose_solarradiation = _('Solar radiation')
verbose_winddir = _('Wind direction')


class AWSStation(CommonAbstractModel):
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    point = models.PointField(
        null=True,
        blank=True,
        verbose_name=verbose_point
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        verbose_name_plural = _('Aws stations')

    def get_absolute_url(self):
        return reverse('aws:awsstation_detail', args=[self.pk])

    def __unicode__(self):
        return '%s' % self.name


class AWSReport(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    awsstation = models.ForeignKey(
        AWSStation,
        verbose_name=verbose_awsstation
    )
    temperature = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        verbose_name=verbose_temperature
    )
    humidity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_humidity
    )
    pressure = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_pressure
    )
    wind_speed = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name=verbose_windspeed
    )
    wind_direction = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_winddir
    )
    day_rain = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_dayrain
    )
    rain_rate = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name=verbose_rainrate
    )
    uv_index = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name=verbose_uvindex
    )
    solar_radiation = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name=verbose_solarradiation
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Aws reports')

    def __unicode__(self):
        return '[%s] - %s' % (self.awsstation, timezone.localtime(self.created))
