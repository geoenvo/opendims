from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import EarlyWarningReport


class EarlyWarningReportAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'created',
        'content',
        'note',
        'published'
    )
    list_display = [
        'title',
        'created',
        'updated',
        'published'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created', 'published']
    search_fields = ['title', 'note']


admin.site.register(EarlyWarningReport, EarlyWarningReportAdmin)
