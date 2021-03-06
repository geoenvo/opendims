from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from reports.models import Disaster
from common.models import CommonAbstractModel


verbose_disaster = _('Disaster')
verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_type = _('Type')
verbose_keyword = _('Keyword')
verbose_name = _('Name')
verbose_status = _('Status')
verbose_source = _('Source')


class Source(CommonAbstractModel):
    TYPE_CHOICES = (
        ('TWITTER', _('Twitter')),
    )
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='TWITTER',
        verbose_name=verbose_type
    )
    disaster = models.ForeignKey(
        Disaster,
        verbose_name=verbose_disaster
    )
    STATUS_CHOICES = (
        ('ACTIVE', _('Active')),
        ('INACTIVE', _('Inactive')),
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='INACTIVE',
        verbose_name=verbose_status
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Sources')

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.type, self.name, self.disaster)


class Keyword(CommonAbstractModel):
    source = models.ForeignKey(
            Source,
            related_name='keywords',
            verbose_name=verbose_source
    )
    keyword = models.CharField(
        max_length=50,
        verbose_name=verbose_keyword
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Keywords')

    def __unicode__(self):
        return '[%s] - %s' % (self.source, self.keyword)
