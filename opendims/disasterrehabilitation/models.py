from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
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
verbose_start = _('Start Date')
verbose_end = _('End Date')
verbose_year = _('Year')
verbose_agency = _('Agency')
verbose_type = _('Type')
verbose_funding = _('Funding')
verbose_activity = _('Activity')
verbose_postassesment = _('Post Assesment')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')

class Agency(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    name = models.CharField(
        max_length=50,
        verbose_name=verbose_name
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    def __unicode__(self):
        return '%s' % self.name

class PostAssesment(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    event = models.ForeignKey(
        Event,
        verbose_name=verbose_event
    )
    name = models.CharField(
        max_length=50,
        verbose_name=verbose_name
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='disasterrehabilitation/postassesment/',
        verbose_name=verbose_file
    )
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'

    def __unicode__(self):
        return '[%s] -  %s' % (self.name, timezone.localtime(self.created))

class Activity(CommonAbstractModel):
    TYPE_CHOICES = (
        ('Physical', _('Physical')),
        ('Non-Physical', _('Non-Physical')),
    )
    FUNDING_CHOICES = (
        ('APBN', _('APBN')),
        ('APBD', _('APBD')),
        ('Society Funds', _('Society Funds')),
        ('CSR', _('CSR')),
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
        verbose_name=verbose_event
    )
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='Physical',
        verbose_name=verbose_type
    )
    start = models.DateTimeField(
        verbose_name=verbose_start
    )
    end = models.DateTimeField(
        verbose_name=verbose_end
    )
    agency = models.ForeignKey(
        Agency,
        verbose_name=verbose_agency
    )
    funding = models.CharField(
        max_length=50,
        choices=FUNDING_CHOICES,
        default='Physical',
        verbose_name=verbose_funding
    )
    year = models.PositiveIntegerField(
        verbose_name=verbose_year
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] -  %s' % (self.name, timezone.localtime(self.created))

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
        null=True,
        blank=True,
        upload_to='disasterrehabilitation/reference/',
        verbose_name=verbose_file
    )
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] -  %s' % (self.name, timezone.localtime(self.created))

class Location(CommonAbstractModel):
    activity = models.ForeignKey(
        Activity,
        null=True,
        blank=True,
        verbose_name=verbose_activity
    )
    postassesment = models.ForeignKey(
        PostAssesment,
        null=True,
        blank=True,
        verbose_name=verbose_postassesment
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
        ordering = ['-pk']
