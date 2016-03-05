from __future__ import unicode_literals

from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from geolevels.models import Province, City, Subdistrict, Village, RW, RT
from .models import Source, Disaster, Event, Report


verbose_mark_unverified = _('Mark Event as Unverified')
verbose_mark_verified = _('Mark Event as Verified')


def make_unverified(modeladmin, request, queryset):
    queryset.update(status='UNVERIFIED')

make_unverified.short_description = verbose_mark_unverified


def make_verified(modeladmin, request, queryset):
    queryset.update(status='VERIFIED')

make_verified.short_description = verbose_mark_verified


class ReportInline(admin.TabularInline):
    model = Report
    extra = 3


class SourceAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class DisasterAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class EventResource(resources.ModelResource):
    province = fields.Field(
        column_name='province',
        attribute='province',
        widget=widgets.ForeignKeyWidget(Province, 'name')
    )
    city = fields.Field(column_name='city', attribute='city', widget=widgets.ForeignKeyWidget(City, 'name'))
    subdistrict = fields.Field(
        column_name='subdistrict',
        attribute='subdistrict',
        widget=widgets.ForeignKeyWidget(Subdistrict, 'name')
    )
    village = fields.Field(column_name='village', attribute='village', widget=widgets.ForeignKeyWidget(Village, 'name'))
    rw = fields.Field(column_name='RW', attribute='rw', widget=widgets.ForeignKeyWidget(RW))
    rt = fields.Field(column_name='RT', attribute='rt', widget=widgets.ForeignKeyWidget(RT, 'name'))
    
    class Meta:
        model = Event
        fields = ('id', 'disaster', 'province', 'city', 'subdistrict', 'village', 'rw', 'rt')
        export_order = fields


verbose_event_details = _('Event details')
verbose_affected_area = _('Affected area')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')


class EventAdmin(ImportExportModelAdmin, ExportActionModelAdmin, LeafletGeoAdmin):
    resource_class = EventResource
    
    # Leaflet widget override
    settings_overrides = {
       'DEFAULT_ZOOM': 11,
    }
    
    fieldsets = [
        (verbose_event_details, {'fields': ['created', 'disaster', 'height', 'magnitude', 'note']}),
        (verbose_affected_area, {'fields': ['province', 'city', 'subdistrict', 'village', 'rw', 'rt', 'point']}),
    ]
    list_display = ['created', 'updated', 'status', 'disaster', 'province_admin_url', 'city_admin_url', 'subdistrict_admin_url', 'village_admin_url', 'rw', 'rt', 'height', 'magnitude', 'note']
    readonly_fields = ['updated']
    ordering = ['-created']
    list_filter = ['created', 'updated', 'status', 'disaster']
    search_fields = ['province__name', 'city__name', 'subdistrict__name', 'village__name', 'note']
    inlines = [ReportInline]
    
    def province_admin_url(self, obj):
        if not obj.province:
            return '-'
        return format_html("<a href='{url}'>{province}</a>", url=obj.province.get_admin_url(), province=obj.province)
    
    province_admin_url.short_description = verbose_province
    
    def city_admin_url(self, obj):
        if not obj.city:
            return '-'
        return format_html("<a href='{url}'>{city}</a>", url=obj.city.get_admin_url(), city=obj.city)
    
    city_admin_url.short_description = verbose_city
    
    def subdistrict_admin_url(self, obj):
        if not obj.subdistrict:
            return '-'
        return format_html("<a href='{url}'>{subdistrict}</a>", url=obj.subdistrict.get_admin_url(), subdistrict=obj.subdistrict)
    
    subdistrict_admin_url.short_description = verbose_subdistrict
    
    def village_admin_url(self, obj):
        if not obj.village:
            return '-'
        return format_html("<a href='{url}'>{village}</a>", url=obj.village.get_admin_url(), village=obj.village)
    
    village_admin_url.short_description = verbose_village
    
    def rw_admin_url(self, obj):
        if not obj.rw:
            return '-'
        return format_html("<a href='{url}'>{rw}</a>", url=obj.rw.get_admin_url(), rw=obj.rw)
    
    rw_admin_url.short_description = verbose_rw
    
    def rt_admin_url(self, obj):
        if not obj.rt:
            return '-'
        return format_html("<a href='{url}'>{rt}</a>", url=obj.rt.get_admin_url(), rt=obj.rt)
    
    rt_admin_url.short_description = verbose_rt


verbose_report_details = _('Report details')
verbose_event = _('Event')


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_report_details, {'fields': ['created', 'updated', 'event', 'source', 'status', 'note']})
    ]
    list_display = ['created', 'updated', 'event_admin_url', 'source', 'status', 'note']
    readonly_fields = ['updated']
    ordering = ['-created']
    list_filter = ['created', 'updated', 'source', 'status']
    search_fields = ['note']
    actions = [make_verified, make_unverified]
    
    def event_admin_url(self, obj):
        if not obj.event:
            return '-'
        return format_html("<a href='{url}'>{event}</a>", url=obj.event.get_admin_url(), event=obj.event)
    
    event_admin_url.short_description = verbose_event


admin.site.register(Source, SourceAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Event, EventAdmin)
