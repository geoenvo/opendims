from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField
from embed_video.fields import EmbedVideoField
from colorfield.fields import ColorField

from common.models import CommonAbstractModel
from common.validators import FileSizeValidator


verbose_created = _('Created')
verbose_start = _('Start')
verbose_end = _('End')
verbose_updated = _('Updated')
verbose_note = _('Note')
verbose_content = _('Content')
verbose_file = _('File')
verbose_title = _('Title')
verbose_slug = _('Slug')
verbose_attachment = _('Attachment')
verbose_author_text = _('Author text')
verbose_slideshow_image = _('Slideshow image')
verbose_slideshow_image_crop = _('Slideshow image crop (770x400 px)')
verbose_slideshow_image_post = _('Slideshow image post (750x390 px)')
verbose_slideshow_image_list = _('Slideshow image list (170x150 px)')
verbose_slideshow_image_thumb = _('Slideshow image thumb (70x70 px)')
verbose_published = _('Published')
verbose_slideshow_enabled = _('Slideshow enabled')
verbose_image = _('Image')
verbose_category = _('Category')
verbose_post = _('Post')
verbose_image_thumb = _('Image thumb (70x70 px)')
verbose_image_preview = _('Image preview (260x180 px)')
verbose_image_list = _('Image list (170x150 px)')
verbose_order = _('Order')
verbose_url = _('Url')
verbose_logo = _('Logo')
verbose_logo_crop = _('Logo crop')
verbose_name = _('Name')


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
        max_length=200,
        db_index=True,
        verbose_name=verbose_title
    )
    slug = models.SlugField(
        max_length=200,
        blank=True,
        db_index=True,
        verbose_name=verbose_slug
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
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=verbose_category
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
    slideshow_image_list = ImageRatioField(
        'slideshow_image',
        '170x150',
        size_warning=True,
        verbose_name=verbose_slideshow_image_list
    )
    slideshow_image_thumb = ImageRatioField(
        'slideshow_image',
        '70x70',
        size_warning=True,
        verbose_name=verbose_slideshow_image_thumb
    )

    class Meta:
        index_together = ['id', 'slug']
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Posts')

    def get_absolute_url(self):
        return reverse('website:post_detail', args=[self.pk, self.slug])

    def __unicode__(self):
        return '[%s] - %s - %s' % (self.title, timezone.localtime(self.created), self.category)


class Attachment(CommonAbstractModel):
    post = models.ForeignKey(
        Post,
        related_name='attachments',
        verbose_name=verbose_post
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=verbose_title
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
        upload_to='website/attachment_file/',
        verbose_name=verbose_file
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='website/attachment_image/',
        validators=[
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_image
    )
    image_preview = ImageRatioField(
        'image',
        '260x180',
        size_warning=True,
        verbose_name=verbose_image_preview
    )
    image_list = ImageRatioField(
        'image',
        '170x150',
        size_warning=True,
        verbose_name=verbose_image_list
    )
    image_thumb = ImageRatioField(
        'image',
        '70x70',
        size_warning=True,
        verbose_name=verbose_image_thumb
    )
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Attachments')

    def __unicode__(self):
        return '[%s] -  %s' % (self.title, timezone.localtime(self.created))


class SiteHeader(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=verbose_title
    )
    start = models.DateField(
        verbose_name=verbose_start
    )
    end = models.DateField(
        verbose_name=verbose_end
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=verbose_updated)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='website/siteheader/',
        validators=[
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_image
    )
    background_color = ColorField(default='#003a6a')
    note = models.TextField(blank=True, verbose_name=verbose_note)
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Site headers')

    def __unicode__(self):
        return '[%s] - %s ~ %s' % (self.title, self.start, self.end)


class Welcome(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=verbose_title
    )
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    content = RichTextField(
        blank=True,
        verbose_name=verbose_content
    )
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Welcomes')

    def __unicode__(self):
        return '[%s] - %s' % (self.title, timezone.localtime(self.created))


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name=verbose_name)
    url = models.URLField(blank=True, verbose_name=verbose_url)
    logo = models.ImageField(
        upload_to='website/partner/',
        validators=[
            FileSizeValidator(1)  # max MB
        ],
        verbose_name=verbose_logo
    )
    logo_crop = ImageRatioField(
        'logo',
        '170x120',
        size_warning=True,
        verbose_name=verbose_logo_crop
    )
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Partners')

    def __unicode__(self):
        return '[%s] - %s' % (self.name, self.url)


class Link(models.Model):
    ORDER_CHOICES = [(i, i) for i in range(11)]
    name = models.CharField(max_length=100, verbose_name=verbose_name)
    url = models.CharField(max_length=200, verbose_name=verbose_url)
    order = models.PositiveIntegerField(
        choices=ORDER_CHOICES,
        default=0,
        verbose_name=verbose_order
    )
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['pk']
        get_latest_by = 'pk'
        verbose_name_plural = _('Links')

    def __unicode__(self):
        return '[%s] - %s' % (self.name, self.url)


class Resource(models.Model):
    ORDER_CHOICES = [(i, i) for i in range(11)]
    name = models.CharField(max_length=100, verbose_name=verbose_name)
    url = models.CharField(max_length=200, verbose_name=verbose_url)
    order = models.PositiveIntegerField(
        choices=ORDER_CHOICES,
        default=0,
        verbose_name=verbose_order
    )
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )



class Video(models.Model):
    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=verbose_created
    )
    title = models.CharField(max_length=100, verbose_name="Judul")
    url = EmbedVideoField(verbose_name='URL')  # same like models.URLField()
    published = models.BooleanField(
        default=False,
        verbose_name=verbose_published
    )

    class Meta:
        ordering = ['created']
        get_latest_by = 'created'
        verbose_name_plural = _('Videos')

    def __unicode__(self):
        return '[%s] - %s' % (self.title, self.url)


# Class For Django Activity Stream
class Verb(models.Model):
    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='actor'
    )
    verb = models.ManyToManyField(
        Verb,
        related_name='verb'
    )

    def __unicode__(self):
        return self.user.username


class Object(models.Model):
    obj_id = models.IntegerField(
        null=True
    )
    obj_text = models.CharField(
        max_length=255
    )
    sub_id = models.IntegerField(
        null=True
    )

    def __unicode__(self):
        return '[%s] - %s' % (self.obj_id, self.obj_text)


