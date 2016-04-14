from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from geolevels.models import Village
from .models import ReportAutoSummary

verbose_ReportAutoSummary = _('ReportAutoSummary')
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
