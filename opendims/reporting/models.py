from __future__ import unicode_literals


from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

from ckeditor.fields import RichTextField

from common.models import CommonAbstractModel
from reports.models import Disaster


verbose_name = _('Name')
verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_author = _('Author')
verbose_content = _('Content')
verbose_disaster_attached = _('Attached disaster')
verbose_template = _('Template')
verbose_text_id = _('Text ID')
verbose_text_author = _('Text author')
verbose_text_title = _('Text title')
verbose_file = _('File')
verbose_type = _('Type')
verbose_status = _('Status')
verbose_report = _('Report')


class Template(CommonAbstractModel):
    name = models.CharField(max_length=100, verbose_name=verbose_name)
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content
    )
    disaster_attached = models.ManyToManyField(
        Disaster,
        blank=True,
        related_name='template_attached',
        verbose_name=verbose_disaster_attached
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.name, timezone.localtime(self.created))


class Report(CommonAbstractModel):
    TYPE_CHOICES = (
        ('DAILY', _('Daily')),
        ('WEEKLY', _('Weekly')),
        ('MONTHLY', _('Monthly')),
        ('YEARLY', _('Yearly')),
    )
    STATUS_CHOICES = (
        ('ACTIVE', _('Active')),
        ('INACTIVE', _('Inactive')),
    )

    template = models.ForeignKey(
        Template,
        related_name='reports',
        verbose_name=verbose_template
    )
    created = models.DateTimeField(
         default=timezone.now,
         verbose_name=verbose_created
     )
    type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        default='DAILY',
        verbose_name=verbose_type
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated
    )
    author = models.ForeignKey(
        'auth.User',
    )
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content
    )
    text_id = models.TextField(
        blank=True,
        verbose_name=verbose_text_id
    )
    text_author = models.TextField(
        blank=True,
        verbose_name=verbose_text_author
    )
    text_title = models.TextField(
        blank=True,
        verbose_name=verbose_text_title
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        verbose_name=verbose_status
    )
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='reporting/report/',
        verbose_name=verbose_file
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.template, timezone.localtime(self.created))

    def save(self, *args, **kwargs):
        report_content = ''
        template = self.template
        if self.text_title:
            report_content = template.content.replace('[[title]]', self.text_title)
        if self.text_author:
            report_content = report_content.replace('[[author]]', self.text_author)
        self.content = report_content

        super(Report, self).save(*args, **kwargs)


class Attachment(CommonAbstractModel):
    report = models.ForeignKey(
        Report,
        related_name='attachments',
        verbose_name=verbose_report
    )
    created = models.DateTimeField(
         default=timezone.now,
         verbose_name=verbose_created
     )
    file = models.FileField(
        blank=True,
        null=True,
        upload_to='reporting/attachment/',
        verbose_name=verbose_file
    )

    class Meta:
        ordering = ['-report']
        get_latest_by = 'created'

    def __unicode__(self):
        return '[%s] - %s' % (self.report, timezone.localtime(self.created))
