from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from .models import WaterGate, WaterLevelReport, MultipleWaterLevelReport


class MultipleWaterLevelReportInline(admin.TabularInline):
    model = MultipleWaterLevelReport
    extra = 1


class WaterLevelReportInline(admin.TabularInline):
    model = WaterLevelReport
    extra = 3

class MultipleWaterLevelReportAdmin(admin.ModelAdmin):
    inlines = [WaterLevelReportInline]

class WaterGateAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_ZOOM': 13,
    }
    fields = (
        'name',
        'point',
        ('siaga_1_min', 'siaga_1_max'),
        ('siaga_2_min', 'siaga_2_max'),
        ('siaga_3_min', 'siaga_3_max'),
        'note'
    )
    list_display = [
        'name',
        'siaga_1_min',
        'siaga_1_max',
        'siaga_2_min',
        'siaga_2_max',
        'siaga_3_min',
        'siaga_3_max'
    ]
    search_fields = ['name', 'note']


class WaterLevelReportAdmin(admin.ModelAdmin):
    fields = (
        'created',
        'watergate',
        'weather',
        'height'
    )
    list_display = [
        'watergate',
        'created',
        'updated',
        'weather',
        'height'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created', 'watergate', 'weather']
    search_fields = ['watergate']
    #inlines = [MultipleWaterLevelReportInline]

admin.site.register(MultipleWaterLevelReport, MultipleWaterLevelReportAdmin)
admin.site.register(WaterGate, WaterGateAdmin)
admin.site.register(WaterLevelReport, WaterLevelReportAdmin)
