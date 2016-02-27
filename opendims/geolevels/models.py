from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Province(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = _('Cities')
    
    def __unicode__(self):
        return self.name


class Subdistrict(models.Model):
    city = models.ForeignKey(City)
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name


class Village(models.Model):
    id = models.BigIntegerField(primary_key=True)
    subdistrict = models.ForeignKey(Subdistrict)
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name


class RW(models.Model):
    id = models.BigIntegerField(primary_key=True)
    village = models.ForeignKey(Village)
    name = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=50, decimal_places=10)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _('RW')
    
    def __unicode__(self):
        return self.name


class RT(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rw = models.ForeignKey(RW)
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(blank=True)
    
    class Meta:
        verbose_name = _('RT')
    
    def __unicode__(self):
        return self.name
