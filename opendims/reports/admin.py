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


class ReportInline(admin.TabularInline):
    model = Report
    extra = 3


class SourceAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class DisasterAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class EventAdmin(ImportExportModelAdmin, ExportActionModelAdmin, admin.OSMGeoAdmin):
    fieldsets = [
        ('Event details', {'fields': ['created', 'disaster', 'height', 'magnitude', 'note']}),
        ('Affected area', {'fields': ['province', 'city', 'subdistrict', 'village', 'rw', 'rt', 'point'], 'classes': ['collapse']}),
    ]
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
    list_filter = ['created', 'disaster']
    search_fields = ['province__name', 'city__name', 'subdistrict__name', 'village__name', 'note']
    inlines = [ReportInline]


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Report details', {'fields': ['created', 'event', 'source', 'status', 'note']})
    ]
    list_display = ['created', 'event', 'source', 'status', 'note']
    ordering = ['-created']
    list_filter = ['created', 'source', 'status']
    search_fields = ['note']
    actions = [make_verified, make_unverified]


admin.site.register(Source, SourceAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Event, EventAdmin)
