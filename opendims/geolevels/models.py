#Future

from __future__ import unicode_literals

#Core django
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Province(models.Model):
	name = models.CharField(max_length=50)
	poly = models.MultiPolygonField(null=True, blank=True)
	note = models.TextField(null=True)


	def __unicode__(self):
		return u'%s' %(self.name)


class City(models.Model):
	name = models.CharField(max_length=50)
	poly = models.MultiPolygonField()
	province = models.ForeignKey(Province)
	note = models.TextField(null=True)


	def __unicode__(self):
		return u'%s' %(self.name)


class Subdistrict(models.Model):
	name = models.CharField(max_length=50)
	poly = models.MultiPolygonField()
	city = models.ForeignKey(City)
	note = models.TextField(null=True)


	def __unicode__(self):
		return u'%s' %(self.name)


class Village(models.Model):
	id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	poly = models.MultiPolygonField(null=True)
	subdistrict = models.ForeignKey(Subdistrict)
	note = models.TextField(null=True)


	def __unicode__(self):
		return u'%s' %(self.name)


class RW(models.Model):
	id = models.BigIntegerField(primary_key=True)
	name = models.CharField(max_length=50, null=True, blank = True)
	area = models.DecimalField(max_digits=50, decimal_places=10)
	poly = models.MultiPolygonField(null=True)
	village = models.ForeignKey(Village)
	note = models.TextField(null=True)


	def __unicode__(self):
		return u'%s' %(self.name)



