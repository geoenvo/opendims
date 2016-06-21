from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import RegexValidator

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
verbose_contactnumber = _('Contact number')
verbose_contact = _('Contact')
verbose_contacts = _('Contacts')


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
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Templates')

    def __unicode__(self):
        return '%s' % self.name


class Contact(CommonAbstractModel):
    name = models.CharField(max_length=100, verbose_name=verbose_name)
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    contact_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        verbose_name=verbose_contactnumber
    )  # validators should be a list

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        return '%s' % self.name


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
    contacts = models.ManyToManyField(
        Contact,
        blank=True,
        related_name='contact_groups',
        verbose_name=verbose_contacts
    )

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Groups')

    def __unicode__(self):
        return '%s' % self.name


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
        blank=True,
        verbose_name=verbose_template
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        verbose_name=verbose_group
    )
    subject = models.CharField(
        max_length=100,
        verbose_name=verbose_subject
    )
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content
    )

    class Meta:
        ordering = ['-pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Messages')

    def __unicode__(self):
        return '[%s] - [%s] - %s' % (self.group, self.template, timezone.localtime(self.created))
