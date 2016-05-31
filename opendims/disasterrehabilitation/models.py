from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.urlresolvers import reverse

from common.models import CommonAbstractModel
from geolevels.models import Province, City, Subdistrict, Village, RW, RT
from reports.models import Event


verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_name = _('Name')
verbose_note = _('Note')
verbose_event = _('Event')
verbose_published = _('Published')
verbose_file = _('File')
verbose_start = _('Start date')
verbose_end = _('End date')
verbose_year = _('Year')
verbose_agency = _('Agency')
verbose_type = _('Type')
verbose_funding = _('Funding')
verbose_activity = _('Activity')
verbose_eventassesment = _('Event assessment')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')
verbose_status = _('Status')


class Agency(CommonAbstractModel):
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = 'agencies'

    def __unicode__(self):
        return '%s' % self.name


class EventAssessment(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated
    )
    event = models.ForeignKey(
        Event,
        verbose_name=verbose_event
    )
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='disasterrehabilitation/eventassessment/',
        verbose_name=verbose_file
    )
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'

    def __unicode__(self):
        return '[%s] -  %s' % (self.name, timezone.localtime(self.created))

    def get_absolute_url(self):
        return reverse('disasterrehabilitation:eventassessment_detail', args=[self.pk])


class Activity(CommonAbstractModel):
    TYPE_CHOICES = (
        ('PHYSICAL', _('PHYSICAL')),
        ('NON-PHYSICAL', _('NON-PHYSICAL')),
    )
    FUNDING_CHOICES = (
        ('APBN', _('APBN')),
        ('APBD', _('APBD')),
        ('CSR', _('CSR')),
        ('PUBLIC', _('Public')),
        ('OTHER', _('Other')),
    )
    STATUS_CHOICES = (
        ('PENDING', _('PENDING')),
        ('IN-PROGRESS', _('IN-PROGRESS')),
        ('COMPLETED', _('COMPLETED')),
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    event = models.ForeignKey(
        Event,
        null=True,
        blank=True,
        verbose_name=verbose_event
    )
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='PHYSICAL',
        verbose_name=verbose_type
    )
    start = models.DateField(
        verbose_name=verbose_start
    )
    end = models.DateField(
        verbose_name=verbose_end
    )
    agency = models.ForeignKey(
        Agency,
        verbose_name=verbose_agency
    )
    funding = models.CharField(
        max_length=50,
        choices=FUNDING_CHOICES,
        default='APBD',
        verbose_name=verbose_funding
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='PENDING',
        verbose_name=verbose_status
    )
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
        verbose_name=verbose_year
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = 'activities'

    def __unicode__(self):
        return '[%s] -  %s' % (self.name, timezone.localtime(self.created))

    def get_absolute_url(self):
        return reverse('disasterrehabilitation:activity_detail', args=[self.pk])


class Reference(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    activity = models.ForeignKey(
        Activity,
        verbose_name=verbose_activity
    )
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    year = models.PositiveIntegerField(
        verbose_name=verbose_year
    )
    file = models.FileField(
        upload_to='disasterrehabilitation/reference/',
        verbose_name=verbose_file
    )
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'

    def __unicode__(self):
        return '[%s] - %s -  %s' % (self.activity, self.name, timezone.localtime(self.created))


class Location(CommonAbstractModel):
    activity = models.ForeignKey(
        Activity,
        null=True,
        blank=True,
        verbose_name=verbose_activity
    )
    eventassessment = models.ForeignKey(
        EventAssessment,
        null=True,
        blank=True,
        verbose_name=verbose_eventassesment
    )
    province = models.ForeignKey(
        Province,
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
        ordering = ['pk']
        get_latest_by = 'pk'

    def __unicode__(self):
        return '[%s] -- [%s]' % (self.activity, self.eventassessment)
