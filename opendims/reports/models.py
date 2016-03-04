from __future__ import unicode_literals

from decimal import Decimal

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import  models
from django.core.validators import MinValueValidator
from django.core import urlresolvers

from geolevels.models import Province, City, Subdistrict, Village, RW, RT


verbose_code = _('Code')
verbose_note = _('Note')
verbose_disaster = _('Disaster')
verbose_point = _('Point')
verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_status = _('Status')
verbose_height = _('Height')
verbose_magnitude = _('Magnitude')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')
verbose_event = _('Event')
verbose_source = _('Source')


class ReportsAbstractModel(models.Model):
    class Meta:
        abstract = True
    
    def get_admin_url(self):
        return urlresolvers.reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=(self.id,))


class Source(ReportsAbstractModel):
    code = models.CharField(primary_key=True, max_length=50, verbose_name=verbose_code)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    def __unicode__(self):
        return '%s' % self.code


class Disaster(ReportsAbstractModel):
    code = models.CharField(primary_key=True, max_length=50, verbose_name=verbose_code)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    def __unicode__(self):
        return '%s' % self.code


class Event(ReportsAbstractModel):
    STATUS_CHOICES = (
        ('ACTIVE', _('Active')),
        ('INACTIVE', _('Inactive')),
    )
    
    disaster = models.ForeignKey(Disaster, verbose_name=verbose_disaster)
    point = models.PointField(null=True, blank=True, verbose_name=verbose_point)
    created = models.DateTimeField(default=timezone.now, verbose_name=verbose_created)
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ACTIVE', verbose_name=verbose_status)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    height = models.PositiveIntegerField(null=True, blank=True, verbose_name=verbose_height)
    magnitude = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], verbose_name=verbose_magnitude)
    province = models.ForeignKey(Province, null=True, blank=True, verbose_name=verbose_province)
    city = models.ForeignKey(City, null=True, blank=True, verbose_name=verbose_city)
    subdistrict = models.ForeignKey(Subdistrict, null=True, blank=True, verbose_name=verbose_subdistrict)
    village = models.ForeignKey(Village, null=True, blank=True, verbose_name=verbose_village)
    rw = models.ForeignKey(RW, null=True, blank=True, verbose_name=verbose_rw)
    rt = models.ForeignKey(RT, null=True, blank=True, verbose_name=verbose_rt)
    
    def __unicode__(self):
        return '[%s] - %s' % (self.disaster, timezone.localtime(self.created))


class Report(ReportsAbstractModel):
    STATUS_CHOICES = (
        ('VERIFIED', _('Verified')),
        ('UNVERIFIED', _('Unverified')),
        ('TBD', _('To be determined')),
    )
    
    event = models.ForeignKey(Event, verbose_name=verbose_event)
    source = models.ForeignKey(Source, verbose_name=verbose_source)
    created = models.DateTimeField(default=timezone.now, verbose_name=verbose_created)
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='TBD', verbose_name=verbose_status)
    note = models.TextField(blank=True, verbose_name=verbose_note)
    
    def __unicode__(self):
        return '[%s] - %s - %s' % (self.event, self.source, self.status)
