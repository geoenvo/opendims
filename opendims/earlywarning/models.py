from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from ckeditor.fields import RichTextField
from common.models import CommonAbstractModel

verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_note = _('Note')
verbose_content = _('Content')
verbose_title = _('Title')


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

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.title, timezone.localtime(self.created))