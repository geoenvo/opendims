#Future
from __future__ import unicode_literals

#Core django
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return u'%s' %(self.name)


class City(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField(null=True, blank=True)
    province = models.ForeignKey(Province)
    note = models.TextField()


    def __unicode__(self):
        return u'%s' %(self.name)


class Subdistrict(models.Model):
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField()
    city = models.ForeignKey(City)
    note = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return u'%s' %(self.name)


class Village(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField()
    subdistrict = models.ForeignKey(Subdistrict)
    note = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return u'%s' %(self.name)


class RW(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank = True)
    area = models.DecimalField(max_digits=50, decimal_places=10)
    polygon = models.MultiPolygonField()
    village = models.ForeignKey(Village)
    note = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return u'%s' %(self.name)


class RT(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    polygon = models.MultiPolygonField()
    note = models.TextField(null=True, blank =True)


    def __unicode__(self):
    	return u'%s' %(self.name)



