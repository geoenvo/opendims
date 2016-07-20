from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

from common.models import CommonAbstractModel


verbose_title = _('Title')
verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_content = _('Content')
verbose_note = _('Note')
verbose_published = _('Published')


class EarlyWarningReport(CommonAbstractModel):
    title = models.CharField(
        max_length=100,
        verbose_name=verbose_title
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Early Warning Reports')

    def __unicode__(self):
        return '[%s] - %s' % (self.title, timezone.localtime(self.created))

    def get_absolute_url(self):
        return reverse('earlywarning:earlywarningreport_detail', args=[self.pk])
