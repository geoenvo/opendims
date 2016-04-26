from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from ckeditor.fields import RichTextField
from common.models import CommonAbstractModel
from common.validators import FileSizeValidator


verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_note = _('Note')
verbose_content = _('Content')
verbose_file = _('File')
verbose_title = _('Title')
verbose_attachment = _('Attachment')
verbose_authortext = _('Author Text')
verbose_slideshowimage = _('Slideshow Image')
verbose_published = _('Published')
verbose_slideshowenabled = _('Slideshow Enabled')
verbose_image = _('Image')
verbose_name = _('Name')
verbose_categories = _('Categories')
verbose_post = _('Post')


class Post(CommonAbstractModel):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    updated = models.DateTimeField(auto_now=True, verbose_name=verbose_updated)
    author = models.ForeignKey(
        'auth.User',
    )
    author_text = models.TextField(
        blank=True,
        verbose_name=verbose_authortext)
    title = models.CharField(
        max_length=100,
        verbose_name=verbose_title
    )
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content
    )
    slideshow_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='website/slideshow_image/',
        validators=[
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_slideshowimage
    )
    published = models.BooleanField(
        default=True,
        verbose_name=verbose_published
    )
    slideshow_enabled = models.BooleanField(
        default=True,
        verbose_name=verbose_slideshowenabled
    )
    categories = models.ManyToManyField(
        'categories.Category',
        blank=True,
        related_name='posts',
        verbose_name=verbose_categories
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s ' % (self.title, timezone.localtime(self.created))


class Attachment(CommonAbstractModel):
    post = models.ForeignKey(
        Post,
        null=True,
        blank=True,
        verbose_name=verbose_post
    )
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
    file = models.FileField(
        null=True,
        blank=True,
        upload_to='website/attachment/',
        verbose_name=verbose_file
    )

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] -  %s' % (self.name, timezone.localtime(self.created))


class SiteHeader(CommonAbstractModel):
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
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='website/siteheader_image/',
        validators=[
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_image
    )
    note = models.TextField(blank=True, verbose_name=verbose_note)

    class Meta:
        ordering = ['-updated', '-created']
        get_latest_by = 'updated'

    def __unicode__(self):
        return '[%s] - %s' % (self.title, timezone.localtime(self.created))
