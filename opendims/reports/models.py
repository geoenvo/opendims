from __future__ import unicode_literals
from decimal import Decimal

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator
from django.core.urlresolvers import reverse
from django import forms

from image_cropping import ImageRatioField

from common.models import CommonAbstractModel
from common.validators import FileSizeValidator
from geolevels.models import Province, City, Subdistrict, Village, RW, RT


verbose_code = _('Code')
verbose_note = _('Note')


class Source(CommonAbstractModel):
    code = models.CharField(
        primary_key=True,
        max_length=50,
        verbose_name=verbose_code
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        verbose_name_plural = _('Sources')

    def __unicode__(self):
        return '%s' % self.note


class Disaster(CommonAbstractModel):
    code = models.CharField(
        primary_key=True,
        max_length=50,
        verbose_name=verbose_code
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        verbose_name_plural = _('Disasters')

    def __unicode__(self):
        return '%s' % self.note


verbose_disaster = _('Disaster')
verbose_point = _('Point')
verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_closed = _('Closed')
verbose_status = _('Status')
verbose_height = _('Height')
verbose_height_min = _('Minimum height')
verbose_magnitude = _('Magnitude')
verbose_depth = _('Depth')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')


class Event(CommonAbstractModel):
    STATUS_CHOICES = (
        ('ACTIVE', _('Active')),
        ('INACTIVE', _('Inactive')),
    )

    disaster = models.ForeignKey(Disaster, verbose_name=verbose_disaster)
    point = models.PointField(
        null=True,
        blank=True,
        verbose_name=verbose_point
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    closed = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=verbose_closed
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        verbose_name=verbose_status
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    height = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_height,
        help_text=_('Unit in cm')
    )
    height_min = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_height_min,
        help_text=_('Unit in cm')
    )
    magnitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name=verbose_magnitude,
        help_text=_('Unit in Scala Richter')
    )
    depth = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name=verbose_depth,
        help_text=_('Unit in km')
    )
    province = models.ForeignKey(
        Province,
        null=True,
        blank=True,
        verbose_name=verbose_province
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        verbose_name=verbose_city
    )
    subdistrict = models.ForeignKey(
        Subdistrict,
        null=True,
        blank=True,
        verbose_name=verbose_subdistrict
    )
    village = models.ForeignKey(
        Village,
        null=True,
        blank=True,
        verbose_name=verbose_village
    )
    rw = models.ForeignKey(RW, null=True, blank=True, verbose_name=verbose_rw)
    rt = models.ForeignKey(RT, null=True, blank=True, verbose_name=verbose_rt)

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Events')

    def get_absolute_url(self):
        return reverse('reports:event_detail', args=[self.pk])

    def __unicode__(self):
        return '[%s] - %s' % (self.disaster, timezone.localtime(self.created).strftime('%Y-%m-%d %H:%M:%S %Z'))


verbose_event = _('Event')
verbose_source = _('Source')


class Report(CommonAbstractModel):
    STATUS_CHOICES = (
        ('VERIFIED', _('Verified')),
        ('UNVERIFIED', _('Unverified')),
        ('PENDING', _('Pending')),
    )

    event = models.ForeignKey(
        Event,
        null=True,
        blank=True,
        related_name='reports',
        verbose_name=verbose_event
    )
    source = models.ForeignKey(Source, verbose_name=verbose_source)
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name=verbose_status
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Reports')

    def get_absolute_url(self):
        return reverse('reports:report_detail', args=[self.pk])

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.event, self.source, self.status)


verbose_image = _('Image')
verbose_order = _('Order')
verbose_published = _('Published')
verbose_image_preview = _('Image preview (260x180 px)')
verbose_image_thumb = _('Image thumb (70x70 px)')
verbose_title = _('Title')


class EventImage(CommonAbstractModel):
    ORDER_CHOICES = [(i, i) for i in range(11)]
    event = models.ForeignKey(
        Event,
        related_name='eventimages',
        verbose_name=verbose_event
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=verbose_title
    )
    order = models.PositiveIntegerField(
        choices=ORDER_CHOICES,
        default=0,
        verbose_name=verbose_order
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='reports/event_image/',
        validators=[
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_image
    )
    image_preview = ImageRatioField(
        'image',
        '260x180',
        size_warning=True,
        verbose_name=verbose_image_preview
    )
    image_thumb = ImageRatioField(
        'image',
        '70x70',
        size_warning=True,
        verbose_name=verbose_image_thumb
    )
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Event images')

    def __unicode__(self):
        return '[%s] -  %s' % (self.event, self.title)


verbose_rt_text = _('RT text')
verbose_evac_point = _('Evacuation point')
verbose_evac_total = _('Evacuated total')
verbose_affected_total = _('Affected (in Person)')
verbose_affected_death = _('Affected death')
verbose_affected_injury = _('Affected injury')
verbose_loss_total = _('Loss total')
verbose_affected_total_in_kk = _('Affected (in KK)')


class EventImpact(CommonAbstractModel):
    event = models.ForeignKey(
        Event,
        related_name='eventimpacts',
        verbose_name=verbose_event
    )
    province = models.ForeignKey(
        Province,
        null=True,
        blank=True,
        verbose_name=verbose_province
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        verbose_name=verbose_city
    )
    subdistrict = models.ForeignKey(
        Subdistrict,
        null=True,
        blank=True,
        verbose_name=verbose_subdistrict
    )
    village = models.ForeignKey(
        Village,
        null=True,
        blank=True,
        verbose_name=verbose_village
    )
    rw = models.ForeignKey(RW, null=True, blank=True, verbose_name=verbose_rw)
    rt = models.ForeignKey(RT, null=True, blank=True, verbose_name=verbose_rt)
    rt_text = models.TextField(
        blank=True,
        verbose_name=verbose_rt_text
    )
    evac_point = models.PointField(
        null=True,
        blank=True,
        verbose_name=verbose_evac_point
    )
    evac_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_evac_total
    )
    affected_total = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_affected_total,
        help_text=_('In Person')
    )
    affected_total_in_kk = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_affected_total_in_kk,
        help_text=_('In KK')
    )

    affected_death = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_affected_death
    )
    affected_injury = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=verbose_affected_injury
    )
    loss_total = models.DecimalField(
        null=True,
        blank=True,
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name=verbose_loss_total
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Event impacts')

    def __unicode__(self):
        return '[%s] - %s' % (self.event, self.note)
