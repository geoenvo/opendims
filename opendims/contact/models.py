from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from common.models import CommonAbstractModel


verbose_created = _('Created')
verbose_name = _('Name')
verbose_email = _('E-mail')
verbose_website = _('Website')
verbose_subject = _('Subject')
verbose_message = _('Message')


class Contact(CommonAbstractModel):
    SUBJECT_CHOICES = (
        ('DISASTER_INFO', _('Disaster information')),
        ('WATERLEVEL_INFO', _('Water level information')),
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    email = models.EmailField(
        verbose_name=verbose_email
    )
    website = models.URLField(
        null=True,
        blank=True,
        verbose_name=verbose_website
    )
    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES,
        default='DISASTER_INFO',
        verbose_name=verbose_subject
    )
    message = models.TextField(
        verbose_name=verbose_message
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.subject, timezone.localtime(self.created), self.name)
