from django.contrib.gis import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from .models import Source, Disaster, Event, Report


def make_unverified(modeladmin, request, queryset):
    queryset.update(status='UNV')

make_unverified.short_description = 'Mark Event as Unverified'

def make_verified(modeladmin, request, queryset):
    queryset.update(status='VER')

make_verified.short_description = 'Mark Event as Verified'


class SourceAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']


class DisasterAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']


class ReportAdmin(admin.ModelAdmin):
    list_display = ['created', 'source', 'event', 'status', 'note']
    ordering = ['-created']
    actions = [make_verified, make_unverified]


class EventAdmin(ImportExportModelAdmin, ExportActionModelAdmin, admin.OSMGeoAdmin):
    list_display = [
        'created',
        'disaster',
        'province',
        'city',
        'subdistrict',
        'village',
        'rw',
        'rt',
        'height',
        'magnitude',
        'note'
    ]
    ordering = ['-created']


admin.site.register(Source, SourceAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Event, EventAdmin)
