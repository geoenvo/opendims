from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import EarlyWarningReport

verbose_earlywarningreport_details = _('Early Warning Report details')


class EarlyWarningReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_earlywarningreport_details, {
            'fields': [
                'title',
                'created',
                'content',
                'note'
            ]
        })
    ]
    list_display = [
        'title',
        'created',
        'updated'
    ]

admin.site.register(EarlyWarningReport, EarlyWarningReportAdmin)
