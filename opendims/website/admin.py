from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from image_cropping import ImageCroppingMixin

from .models import Attachment, Post, SiteHeader, Welcome


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
    fieldsets = [
        (verbose_siteheader_details, {
            'fields': [
                'title',
                'created',
                'image',
                'note',
                'published'
            ]
        })
    ]
    list_display = [
        'title',
        'created',
        'updated',
        'published'
    ]


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


admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(SiteHeader, SiteHeaderAdmin)
admin.site.register(Welcome, WelcomeAdmin)
