from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models

from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField

from common.models import CommonAbstractModel
from common.validators import FileSizeValidator


verbose_created = _('Created')
verbose_updated = _('Updated')
verbose_note = _('Note')
verbose_content = _('Content')
verbose_file = _('File')
verbose_title = _('Title')
verbose_attachment = _('Attachment')
verbose_author_text = _('Author text')
verbose_slideshow_image = _('Slideshow image')
verbose_slideshow_image_crop = _('Slideshow image crop (770x400 px)')
verbose_slideshow_image_post = _('Slideshow image post (750x390 px)')
verbose_slideshow_image_thumb = _('Slideshow image thumb (70x70 px)')
verbose_published = _('Published')
verbose_slideshow_enabled = _('Slideshow enabled')
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
        verbose_name=verbose_author_text)
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
        verbose_name=verbose_slideshow_image
    )
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )
    slideshow_enabled = models.BooleanField(
        default=False,
        verbose_name=verbose_slideshow_enabled
    )
    categories = models.ManyToManyField(
        'categories.Category',
        blank=True,
        related_name='posts',
        verbose_name=verbose_categories
    )
    slideshow_image_crop = ImageRatioField(
        'slideshow_image',
        '770x400',
        size_warning=True,
        verbose_name=verbose_slideshow_image_crop
    )
    slideshow_image_post = ImageRatioField(
        'slideshow_image',
        '750x390',
        size_warning=True,
        verbose_name=verbose_slideshow_image_post
    )
    slideshow_image_thumb = ImageRatioField(
        'slideshow_image',
        '70x70',
        size_warning=True,
        verbose_name=verbose_slideshow_image_thumb
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
