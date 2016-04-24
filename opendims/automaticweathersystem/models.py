from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

from common.models import CommonAbstractModel


verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_point = _('Point')
verbose_name = _('Name')
verbose_note = _('Note')
verbose_awsstation = _('AWS Station')
verbose_temp = _('Temperature')
verbose_humid = _('Humidity')
verbose_pressure = _('Pressure')
verbose_windspeed = _('Wind Speed')
verbose_winddir = _('Wind Direction')
verbose_dayrain = _('Day Rain')
verbose_rainrate = _('Rain Rate')
verbose_uvindex = _('UV Index')
verbose_solarradiation = _('Solar Radiation')
verbose_winddir = _('Wind Direction')


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

    def __unicode__(self):
        return '[%s]' % (self.name)


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
    temperature = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_temp
    )
    humidity = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_humid
    )
    pressure = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_pressure
    )
    wind_speed = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_windspeed
    )
    wind_direction = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_winddir
    )
    day_rain = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_dayrain
    )
    rain_rate = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_rainrate
    )
    uv_index = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_uvindex
    )
    solar_radiation = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_solarradiation
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.awsstation, timezone.localtime(self.created))
