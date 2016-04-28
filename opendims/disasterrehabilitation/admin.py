from __future__ import unicode_literals

from django.contrib.gis import admin
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from import_export import forms
from geolevels.models import Province, City, Subdistrict, Village, RW, RT
from .models import Agency, PostAssesment, Activity, Reference, Location
from .forms import LocationForm
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')


class ActivityLocationInline(admin.TabularInline):
    form = LocationForm
    model = Location
    fieldsets = [
        ('LOCATION', {
            'fields': [
                'activity',
                'province',
                'city',
                'subdistrict',
                'village',
                'rw',
                'rt'
            ]
        })
    ]
    extra = 1

class PostAssesmentLocationInline(admin.TabularInline):
    form = LocationForm
    model = Location
    fieldsets = [
        ('LOCATION', {
            'fields': [
                'postassesment',
                'province',
                'city',
                'subdistrict',
                'village',
                'rw',
                'rt'
            ]
        })
    ]
    extra = 1

class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 1

class AgencyAdmin(admin.ModelAdmin):
    list_display = ['created', 'name', 'note']
    ordering = ['created']

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['created', 'name', 'year']
    ordering = ['-updated', '-created']

class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ['province', 'city', 'subdistrict', 'village', 'rw', 'rt']
    ordering = ['city']

    def province_admin_url(self, obj):
        if not obj.province:
            return None
        return format_html(
            "<a href='{url}'>{province}</a>",
            url=obj.province.get_admin_url(),
            province=obj.province
        )

    province_admin_url.short_description = verbose_province

    def city_admin_url(self, obj):
        if not obj.city:
            return None
        return format_html(
            "<a href='{url}'>{city}</a>",
            url=obj.city.get_admin_url(),
            city=obj.city
        )

    city_admin_url.short_description = verbose_city

    def subdistrict_admin_url(self, obj):
        if not obj.subdistrict:
            return None
        return format_html(
            "<a href='{url}'>{subdistrict}</a>",
            url=obj.subdistrict.get_admin_url(),
            subdistrict=obj.subdistrict
        )

    subdistrict_admin_url.short_description = verbose_subdistrict

    def village_admin_url(self, obj):
        if not obj.village:
            return None
        return format_html(
            "<a href='{url}'>{village}</a>",
            url=obj.village.get_admin_url(),
            village=obj.village
        )

    village_admin_url.short_description = verbose_village

    def rw_admin_url(self, obj):
        if not obj.rw:
            return None
        return format_html(
            "<a href='{url}'>{rw}</a>",
            url=obj.rw.get_admin_url(),
            rw=obj.rw
        )

    rw_admin_url.short_description = verbose_rw

    def rt_admin_url(self, obj):
        if not obj.rt:
            return None
        return format_html(
            "<a href='{url}'>{rt}</a>",
            url=obj.rt.get_admin_url(),
            rt=obj.rt
        )

    rt_admin_url.short_description = verbose_rt

class PostAssesmentAdmin(admin.ModelAdmin):
    inlines = [PostAssesmentLocationInline]
    exclude = ['rw']
    list_display = ['created', 'name','published', 'note']
    ordering = ['created']

verbose_activity_details = _('ACTIVITY DETAILS')

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_activity_details, {
            'fields': [
                'created',
                'event',
                'name',
                'type',
                ('start', 'end'),
                ('agency', 'funding', 'year'),
                'note',
                'published'
            ]
        })
    ]
    inlines = [ReferenceInline, ActivityLocationInline]
    list_display = ['created', 'name', 'start', 'end', 'published', 'year']
    ordering = ['-updated', '-created']


admin.site.register(Agency, AgencyAdmin)
admin.site.register(PostAssesment, PostAssesmentAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Activity, ActivityAdmin)
