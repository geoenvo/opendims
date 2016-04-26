from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import Attachment, Post, SiteHeader


verbose_attachment_details = _('Attachment details')
verbose_post_details = _('Post details')
verbose_siteheader_details = _('Site Header details')
verbose_categories = _('Categories')


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1


class AttachmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_attachment_details, {
            'fields': [
                'name',
                'created',
                'file'
            ]
        })
    ]
    list_display = [
        'name',
        'created',
        'updated'
    ]


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_post_details, {
            'fields': [
                'title',
                'author',
                'created',
                'categories',
                'author_text',
                'content',
                ('slideshow_image', 'slideshow_enabled'),
                'published'
            ]
        })
    ]
    list_display = [
        'title',
        'created',
        'updated',
        'author',
        'published',
        'categories_list'
    ]

    def categories_list(self, obj):
        return ", ".join([category.name for category in obj.categories.order_by('name')])

    categories_list.short_description = verbose_categories
    inlines = [AttachmentInline]


class SiteHeaderAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_siteheader_details, {
            'fields': [
                'title',
                'created',
                'image',
                'note'
            ]
        })
    ]
    list_display = [
        'title',
        'created',
        'updated'
    ]

admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(SiteHeader, SiteHeaderAdmin)
