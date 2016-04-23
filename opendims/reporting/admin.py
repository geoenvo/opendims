from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import Template, Report, Attachment
from .forms import ReportForm


verbose_report_details = _('Report details')
verbose_report_content = _('Report content')
verbose_report_output = _('Report output')
verbose_template_details = _('Template details')
verbose_attachment_details = _('Report details')
verbose_disaster_attached = _('Disaster attached')


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 3


class ReportAdmin(admin.ModelAdmin):
    form = ReportForm
    fieldsets = [
        (verbose_report_details, {
            'fields': [
                'created',
                'author',
                ('type', 'status'),
                ('start', 'end')
            ]
        }),
        (verbose_report_content, {
            'fields': [
                'replace_report_content',
                'template',
                'date',
                'text_id',
                'text_title',
                'text_author',
                'content'
            ]
        }),
        (verbose_report_output, {
            'fields': [
                'file'
            ]
        })
    ]
    list_display = [
        'template',
        'created',
        'updated',
        'type',
        'status',
        'author',
        'file'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['template', 'created', 'updated']
    search_fields = ['author', 'file', 'template']
    inlines = [AttachmentInline]


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
        'disaster_attached_list'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['name', 'created', 'updated']
    search_fields = ['name']

    def disaster_attached_list(self, obj):
        return ", ".join([disaster.code for disaster in obj.disaster_attached.order_by('code')])

    disaster_attached_list.short_description = verbose_disaster_attached


class AttachmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_attachment_details, {
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
        'file'
    ]
    ordering = ['-created']
    list_filter = ['created']
    search_fields = ['file']


admin.site.register(Template, TemplateAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Attachment, AttachmentAdmin)
