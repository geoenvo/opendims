from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin


from .models import Template, Report, Attachment
from .tasks import generate_pdf_report
from .forms import ReportForm


verbose_report_details = _('Report details')
verbose_report_content = _('Report content')
verbose_report_output = _('Report output')
verbose_disaster_attached = _('Disaster attached')


class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 3


class AttachmentInLine (admin.TabularInline):
    model = Attachment
    extra = 1


class ReportAdmin(admin.ModelAdmin):
    form = ReportForm

    def save_model(self, request, obj, form, change):
        """
        Write the attached disaster files.
        """
        obj.save()

        generate_pdf_report.delay(obj.id)

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
    date_hierarchy = 'created'
    list_filter = ['template', 'created']
    search_fields = ['author', 'template']
    inlines = [AttachmentInline]


class TemplateAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'created',
        'content',
        'disaster_attached'
    )
    list_display = [
        'name',
        'created',
        'updated',
        'disaster_attached_list'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created']
    search_fields = ['name']

    def disaster_attached_list(self, obj):
        return ", ".join([disaster.code for disaster in obj.disaster_attached.order_by('code')])

    disaster_attached_list.short_description = verbose_disaster_attached


class AttachmentAdmin(admin.ModelAdmin):
    fields = (
        'report',
        'created',
        'file'
    )
    list_display = [
        'report',
        'created',
        'file'
    ]
    ordering = ['-created']
    list_filter = ['created']
    date_hierarchy = 'created'


admin.site.register(Template, TemplateAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Attachment, AttachmentAdmin)
