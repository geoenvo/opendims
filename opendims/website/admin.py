from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Attachment, Post, SiteHeader, Welcome, Partner, Link, Resource
from .forms import SiteHeaderForm


verbose_attachment_details = _('Attachment details')
verbose_attachment_image = _('Attachment image')
verbose_post_details = _('Post details')
verbose_siteheader_details = _('Site header details')
verbose_category = _('Category')


class AttachmentInline(ImageCroppingMixin, admin.TabularInline):
    model = Attachment
    extra = 3


class AttachmentAdmin(ImageCroppingMixin, admin.ModelAdmin):
    fieldsets = [
        (verbose_attachment_details, {
            'fields': [
                'title',
                'created',
                'published',
                'file'
            ]
        }),
        (verbose_attachment_image, {
            'fields': [
                'image',
                'image_preview',
                'image_list',
                'image_thumb'
            ]
        })
    ]
    list_display = [
        'title',
        'post',
        'created',
        'updated',
        'published'
    ]
    ordering = ['-updated', '-created']
    list_filter = ['created', 'published']


class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    fieldsets = [
        (verbose_post_details, {
            'fields': [
                'title',
                'slug',
                'author',
                'created',
                'category',
                'author_text',
                'content',
                'slideshow_enabled',
                'slideshow_image',
                'slideshow_image_post',
                ('slideshow_image_crop', 'slideshow_image_list', 'slideshow_image_thumb'),
                'published'
            ]
        })
    ]
    list_display = [
        'title',
        'created',
        'updated',
        'author',
        'category',
        'slideshow_enabled',
        'published'
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created', 'updated', 'published', 'slideshow_enabled']
    search_fields = ['title']
    inlines = [AttachmentInline]


class SiteHeaderAdmin(admin.ModelAdmin):
    form = SiteHeaderForm
    fieldsets = [
        (verbose_siteheader_details, {
            'fields': [
                'title',
                'start',
                'end',
                'image',
                'note',
                'published'
            ]
        })
    ]
    list_display = [
        'title',
        'start',
        'end',
        'updated',
        'published'
    ]
    readonly_fields = ['updated']


class WelcomeAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'created',
        'content',
        'published'
    )
    list_display = [
        'title',
        'created',
        'published'
    ]
    date_hierarchy = 'created'
    list_filter = ['created', 'published']
    search_fields = ['title']


class PartnerAdmin(ImageCroppingMixin, admin.ModelAdmin):
    fields = (
        'name',
        'url',
        'logo',
        'logo_crop',
        'published'
    )
    list_display = [
        'name',
        'url',
        'published'
    ]
    list_filter = ['name', 'published']
    search_fields = ['name']


class LinkAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'order',
        'url',
        'published'
    )
    list_display = [
        'name',
        'order',
        'url',
        'published'
    ]
    list_filter = ['order', 'published']
    search_fields = ['name']


class ResourceAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'order',
        'url',
        'published'
    )
    list_display = [
        'name',
        'order',
        'url',
        'published'
    ]
    list_filter = ['order', 'published']
    search_fields = ['name']

admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(SiteHeader, SiteHeaderAdmin)
admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Resource, ResourceAdmin)
