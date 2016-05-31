from __future__ import unicode_literals
import datetime

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.gis import admin
from django.template.loader import get_template
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

from xhtml2pdf import pisa

from .models import Template, Report, Attachment
from .forms import ReportForm
from reports.models import Event


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

        for disaster in obj.template.disaster_attached.all():
            try:
                template = get_template('reporting/report_' + disaster.code + '.html')
                events = Event.objects.filter(disaster__code=disaster.code)

                if obj.start and not obj.end:
                    start = datetime.date(
                        obj.start.year,
                        obj.start.month,
                        obj.start.day
                    )
                    events = events.filter(created__date=start)

                if obj.start and obj.end:
                    events = events.filter(
                        created__range=(obj.start, obj.end)
                    )
                html = template.render({'events': events})
                pdf_disaster_temp = NamedTemporaryFile()

                pisa.CreatePDF(
                    html.encode('utf-8'),
                    dest=pdf_disaster_temp,
                    encoding='utf-8'
                )
                attachment_created = timezone.localtime(timezone.now())
                pdf_disaster_filename = "{}__{}{}".format(
                    attachment_created.strftime('%Y%m%d-%H%M'),
                    disaster.code,
                    '.pdf'
                )

                attachment = Attachment()
                attachment.report = obj
                attachment.created = attachment_created
                attachment.file.save(pdf_disaster_filename, File(pdf_disaster_temp), save=False)
                attachment.save()
            except:
                pass

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
