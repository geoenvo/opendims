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
verbose_name = _('Name')
verbose_template = _('Template')
verbose_group = _('Group')
verbose_subject = _('Subject')
verbose_contactnumber = _('Contact Number')
verbose_contact = _('Contact')


class Template(CommonAbstractModel):
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
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

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.name, timezone.localtime(self.created))


class Group(CommonAbstractModel):
    name = models.CharField(
        max_length=100,
        verbose_name=verbose_name
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.name, timezone.localtime(self.created))


class Message(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    template = models.ForeignKey(
        Template,
        null=True,
        verbose_name=verbose_template
    )
    group = models.ForeignKey(
        Group,
        null=True,
        verbose_name=verbose_group
    )
    subject = models.CharField(
        max_length=100,
        verbose_name=verbose_subject)
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content)

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.group, self.template, timezone.localtime(self.created))


class Contact(CommonAbstractModel):
    name = models.CharField(max_length=100, verbose_name=verbose_name)
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    contact_number = models.PositiveIntegerField(
        default=0,
        verbose_name=verbose_contactnumber
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s ' % (self.name, timezone.localtime(self.created))


class ContactGroup(CommonAbstractModel):
    contact = models.ForeignKey(
        Contact,
        null=True,
        verbose_name=verbose_contact
    )
    group = models.ForeignKey(
        Group,
        null=True,
        verbose_name=verbose_group
    )

    class Meta:
        ordering = ['-group']

    def __unicode__(self):
        return '[%s] - %s' % (self.group, self.group)
