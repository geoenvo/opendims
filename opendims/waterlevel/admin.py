from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import WaterGate, WaterLevelReport


verbose_watergate_details = _('Water Gate details')
verbose_Location = _('Location')
verbose_waterlevelreport_details = _('Water Level Report details')


class WaterGateAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_watergate_details, {
            'fields': [
                'name',
                'point',
                ('siaga_1_min','siaga_1_max'),
                ('siaga_2_min','siaga_2_max'),
                ('siaga_3_min','siaga_3_max'),
                'note'
            ]})
        ]

    list_display = [
    'name',
    'point',
    'siaga_1_max',
    'siaga_2_max',
    'siaga_3_max'
]


class WaterLevelReportAdmin(admin.ModelAdmin):

    fieldsets = [
        (verbose_waterlevelreport_details, {
            'fields': [
                'created',
                'watergate',
                'weather',
                'height'
            ]
        })
    ]
    list_display = [
        'created',
        'updated',
        'watergate',
        'weather',
        'height'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['watergate', 'weather', 'created', 'updated']
    search_fields = ['note']


admin.site.register(WaterGate, WaterGateAdmin)
admin.site.register(WaterLevelReport, WaterLevelReportAdmin)
