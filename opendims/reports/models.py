from __future__ import unicode_literals

from decimal import Decimal

from django.utils import timezone
from django.contrib.gis.db import  models
from django.core.validators import MinValueValidator

from geolevels.models import Province, City, Subdistrict, Village, RW, RT


class Source(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s' % self.code


class Disaster(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s' % self.code


class Event(models.Model):
    disaster = models.ForeignKey(Disaster)
    point = models.PointField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    magnitude = models.DecimalField(
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.01'))
        ]
    )
    province = models.ForeignKey(Province, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    subdistrict = models.ForeignKey(Subdistrict, null=True, blank=True)
    village = models.ForeignKey(Village, null=True, blank=True)
    rw = models.ForeignKey(RW, null=True, blank=True)
    rt = models.ForeignKey(RT, null=True, blank=True)
    
    def __unicode__(self):
        return '[%s] - %s' % (self.disaster, timezone.localtime(self.created))


class Report(models.Model):
    STATUS_CHOICES = (
        ('VER', 'Verified'),
        ('UNV', 'Unverified'),
        ('TBD', 'To Be Determined'),
    )
    
    event = models.ForeignKey(Event)
    source = models.ForeignKey(Source)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='TBD')
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return '[%s] - %s - %s' % (self.event, self.source, self.status)
