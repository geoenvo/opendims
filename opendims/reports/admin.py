from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from .models import Source, Disaster, Event, Report


def make_unverified(modeladmin, request, queryset):
    queryset.update(status='UNVERIFIED')

make_unverified.short_description = _('Mark Event as Unverified')

def make_verified(modeladmin, request, queryset):
    queryset.update(status='VERIFIED')

make_verified.short_description = _('Mark Event as Verified')


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
        (_('Event details'), {'fields': ['created', 'disaster', 'height', 'magnitude', 'note']}),
        (_('Affected area'), {'fields': ['province', 'city', 'subdistrict', 'village', 'rw', 'rt', 'point'], 'classes': ['collapse']}),
    ]
    list_display = ['created', 'updated', 'status', 'disaster', 'province', 'city', 'subdistrict', 'village', 'rw', 'rt', 'height', 'magnitude', 'note']
    readonly_fields = ['updated']
    ordering = ['-created']
    list_filter = ['created', 'updated', 'status', 'disaster']
    search_fields = ['province__name', 'city__name', 'subdistrict__name', 'village__name', 'note']
    inlines = [ReportInline]


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Report details'), {'fields': ['created', 'updated', 'event', 'source', 'status', 'note']})
    ]
    list_display = ['created', 'updated', 'event', 'source', 'status', 'note']
    readonly_fields = ['updated']
    ordering = ['-created']
    list_filter = ['created', 'updated', 'source', 'status']
    search_fields = ['note']
    actions = [make_verified, make_unverified]


admin.site.register(Source, SourceAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Event, EventAdmin)
