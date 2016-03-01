from __future__ import unicode_literals

from django.utils import timezone
from django.contrib.gis.db import  models

from geolevels.models import Province, City, Subdistrict, Village, RW, RT


class Source(models.Model):
    PK = models.CharField(max_length=50, unique=True)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s' % self.PK


class Disaster(models.Model):
    PK = models.CharField(max_length=50, unique=True) # TODO: make PK
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return '%s' % self.PK


class Event(models.Model):
    disaster = models.ForeignKey(Disaster)
    point = models.PointField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    magnitude = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=2) # TODO: positive only
    province = models.ForeignKey(Province, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    subdistrict = models.ForeignKey(Subdistrict, null=True, blank=True)
    village = models.ForeignKey(Village, null=True, blank=True)
    rw = models.ForeignKey(RW, null=True, blank=True)
    rt = models.ForeignKey(RT, null=True, blank=True)
    objects = models.GeoManager()
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
