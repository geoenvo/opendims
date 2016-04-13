from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import Template, Report, Attachment

verbose_template_details = _('Template details')
verbose_report_details = _('Report details')
verbose_set_active = _('Set Template as Active')
verbose_set_inactive = _('Set Template as Inactive')


def set_inactive(modeladmin, request, queryset):
    queryset.update(status='INACTIVE')

set_inactive.short_description = verbose_set_inactive


def set_active(modeladmin, request, queryset):
    queryset.update(status='ACTIVE')

set_active.short_description = verbose_set_active


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_template_details, {
            'fields': [
                'template',
                'type',
                'status',
                'created',
                'content',
                'author',
                'text_author',
                'text_title',
                'file'
            ]
        })
    ]
    list_display = [
        'template',
        'type',
        'status',
        'updated',
        'content',
        'author',
        'text_author',
        'text_title',
        'file'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['content', 'template', 'created', 'updated']
    search_fields = ['file', 'author']


class TemplateAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_template_details, {
            'fields': [
                'name',
                'created',
                'content',
                'disaster_attached'
            ]
        })
    ]
    list_display = [
        'name',
        'created',
        'updated',
        'content',
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['content', 'name', 'created', 'updated']
    search_fields = ['type']


class AttachmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_template_details, {
            'fields': [
                'report',
                'created',
                'file'
            ]
        })
    ]
    list_display = [
        'report',
        'created',
        'file',
    ]
    ordering = ['created']
    list_filter = ['created']
    search_fields = ['file']


admin.site.register(Template, TemplateAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Attachment, AttachmentAdmin)
