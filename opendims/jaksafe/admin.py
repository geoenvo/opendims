from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import ReportAutoSummary


class ReportAutoSummaryAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'village',
        'rw',
        'damage_total',
        'loss_total',
        'note'
    ]
    ordering = ['-created']
    list_filter = ['created']
    search_fields = ['note']

admin.site.register(ReportAutoSummary, ReportAutoSummaryAdmin)
