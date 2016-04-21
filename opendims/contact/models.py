from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.gis.db import models
from common.models import CommonAbstractModel

verbose_created = _('Created')
verbose_name = _('Name')
verbose_email = _('E-Mail')
verbose_website = _('Website')
verbose_subject = _('Subject')
verbose_message = _('Message')

class Contact(CommonAbstractModel):
    SUBJECT_CHOICES = (
        ('D', _('Disaster Information')),
        ('W', _('Waterlevel Information')),
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
        blank=True, null=True,
        verbose_name=verbose_website
    )
    subject = models.CharField(
        max_length=50,
        choices=SUBJECT_CHOICES,
        default='D',
        verbose_name=verbose_subject
    )
    message = models.TextField(
        verbose_name=verbose_message
    )

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'

    def __unicode__(self):
        return '[%s] - %s' % (self.subject, self.name)
