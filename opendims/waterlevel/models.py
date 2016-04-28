from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

from common.models import CommonAbstractModel


verbose_point = _('Point')
verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_height = _('Height')
verbose_weather = _('Weather')
verbose_note = _('Note')
verbose_code = _('Code')
verbose_watergate = _('Water gate')
verbose_name = _('Name')
verbose_siaga1min = _('Siaga 1 min')
verbose_siaga1max = _('Siaga 1 max')
verbose_siaga2min = _('Siaga 2 min')
verbose_siaga2max = _('Siaga 2 max')
verbose_siaga3min = _('Siaga 3 min')
verbose_siaga3max = _('Siaga 3 max')


class WaterGate(CommonAbstractModel):
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    point = models.PointField(
        null=True,
        blank=True,
        verbose_name=verbose_point
    )
    siaga_1_min = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_siaga1min
    )
    siaga_1_max = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_siaga1max
    )
    siaga_2_min = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_siaga2min
    )
    siaga_2_max = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_siaga2max
    )
    siaga_3_min = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_siaga3min
    )
    siaga_3_max = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_siaga3max
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    def __unicode__(self):
        return '[%s]' % (self.name)

    def get_absolute_url(self):
        return reverse('waterlevel:watergate_detail', args=[self.pk])


class WaterLevelReport(CommonAbstractModel):
    WEATHER_CHOICES = (
        ('T', _('Clear')),
        ('MT', _('Slightly cloudy')),
        ('M', _('Cloudy')),
        ('G', _('Drizzle')),
        ('H', _('Rain')),
    )

    height = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_height
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    weather = models.CharField(
        max_length=50,
        choices=WEATHER_CHOICES,
        default='T',
        verbose_name=verbose_weather
    )
    watergate = models.ForeignKey(
        WaterGate,
        related_name='waterlevelreports',
        verbose_name=verbose_watergate
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.watergate, self.height, self.weather)

    def get_threshold_level(self):
        threshold_level = ''
        if self.height < self.watergate.siaga_3_min:
            threshold_level = 'SIAGA-4'
        elif self.height >= self.watergate.siaga_3_min and self.height <= self.watergate.siaga_3_max:
            threshold_level = 'SIAGA-3'
        elif self.height >= self.watergate.siaga_2_min and self.height <= self.watergate.siaga_2_max:
            threshold_level = 'SIAGA-2'
        elif self.height >= self.watergate.siaga_1_min:
            threshold_level = 'SIAGA-1'
        return threshold_level
