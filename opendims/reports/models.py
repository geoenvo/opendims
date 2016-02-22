#Future
from __future__ import unicode_literals


# Django
from django.db import models
from django.utils import timezone
from django.contrib.gis.db import  models
from django.contrib.gis import admin
from django.contrib.gis.geos import *

#Third Party
from decimal import Decimal

class Source(models.Model):
	source =models.CharField(max_length=50)
	note =models.TextField()

	def __str__(self):
		return '%s' %self.source

class Disaster(models.Model):
	code =models.CharField(max_length=50, unique=True)
	note =models.TextField()

	def __str__(self):
		return "%s" %(self.code)

	def __unicode__(self):
		return u'%s' % (self.code)

class Event(models.Model):
	code=models.ForeignKey(Disaster, on_delete=models.CASCADE)
	point=models.PointField(null=True, blank=True)
	created=models.DateTimeField()
	note=models.TextField()
	height=models.PositiveIntegerField(default=0)
	magnitude=models.DecimalField(max_digits=50, decimal_places=4, default=Decimal('0.0000'))

	def __str__(self):
		return '%s' %(self.code)


class Report(models.Model):

	STATUS_CHOICES=(

		('Ver', 'Verified'),
		('UN', 'Unverified'),
		('TBD', 'To be Determined'),
	)

	source=models.ForeignKey(Source, on_delete=models.CASCADE)
	event=models.ForeignKey(Event)
	time=models.DateTimeField()
	status =models.CharField(max_length=50, choices=STATUS_CHOICES, default='TBD')
	note=models.TextField()

	def __str__(self):
		return '(%s) %s %s' %(self.event, self.time, self.status)
# Create your models here.
