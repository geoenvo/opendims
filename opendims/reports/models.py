#Future
from __future__ import unicode_literals

#Standard Library
from decimal import Decimal

# Core Django
from django.utils import timezone
from django.contrib.gis.db import  models
from django.contrib.gis import admin


#Third Party


class Source(models.Model):
	code = models.CharField(max_length=50)
	note = models.TextField(null=True)


	def __unicode__(self):
		return u'%s' %self.code


class Disaster(models.Model):
	code = models.CharField(max_length=50, unique=True)
	note = models.TextField()


	def __unicode__(self):
		return u'%s' % (self.code)


class Event(models.Model):
	disaster = models.ForeignKey(Disaster)
	point = models.PointField(null=True, blank=True)
	created = models.DateTimeField()
	note = models.TextField()
	height = models.PositiveIntegerField(default=0)
	magnitude = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))


	def __unicode__(self):
		return u'%s' %(self.disaster)


class Report(models.Model):

	STATUS_CHOICES = (

		('Ver', 'Verified'),
		('UN', 'Unverified'),
		('TBD', 'To be Determined'),
	)
	
	event = models.ForeignKey(Event)
	source = models.ForeignKey(Source)
	created = models.DateTimeField()
	status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='TBD')
	note = models.TextField()


	def __unicode__(self):
		return u'(%s) %s %s' %(self.event, self.created, self.status)

