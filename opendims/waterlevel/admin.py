from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from .models import WaterGate, WaterLevelReport


verbose_watergate_details = _('Water Gate details')
verbose_waterlevelreport_details = _('Water Level Report details')


class WaterGateAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_ZOOM': 13,
    }

    fieldsets = [
        (verbose_watergate_details, {
            'fields': [
                'name',
                'point',
                ('siaga_1_min', 'siaga_1_max'),
                ('siaga_2_min', 'siaga_2_max'),
                ('siaga_3_min', 'siaga_3_max'),
                'note'
            ]
        })
    ]
    list_display = [
        'name',
        'siaga_1_min',
        'siaga_1_max',
        'siaga_2_min',
        'siaga_2_max',
        'siaga_3_min',
        'siaga_3_max'
    ]
    search_fields = ['note', 'name']


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
    search_fields = ['created', 'watergate', 'weather']


admin.site.register(WaterGate, WaterGateAdmin)
admin.site.register(WaterLevelReport, WaterLevelReportAdmin)
