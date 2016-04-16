from __future__ import unicode_literals

from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

import django
from django.utils.encoding import force_text
from django.http import HttpResponse
from django.template.response import TemplateResponse

from import_export import forms
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from common.admin import LeafletGeoAdminMixin
from .models import Source, Disaster, Event, Report, EventImage, EventImpact
from .forms import EventForm, EventImpactForm
from .resources import EventResource


verbose_set_active = _('Set Event as Active')
verbose_set_inactive = _('Set Event as Inactive')
verbose_set_unverified = _('Set Event as Unverified')
verbose_set_verified = _('Set Event as Verified')


def set_unverified(modeladmin, request, queryset):
    queryset.update(status='UNVERIFIED')

set_unverified.short_description = verbose_set_unverified


def set_verified(modeladmin, request, queryset):
    queryset.update(status='VERIFIED')

set_verified.short_description = verbose_set_verified


def set_inactive(modeladmin, request, queryset):
    queryset.update(status='INACTIVE')

set_inactive.short_description = verbose_set_inactive


def set_active(modeladmin, request, queryset):
    queryset.update(status='ACTIVE')

set_active.short_description = verbose_set_active


class ReportInline(admin.TabularInline):
    model = Report
    extra = 1


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


class EventImpactInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = EventImpact
    form = EventImpactForm
    extra = 1


class SourceAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


class DisasterAdmin(admin.ModelAdmin):
    list_display = ['code', 'note']
    ordering = ['code']


verbose_event_details = _('Event details')
verbose_affected_area = _('Affected area')
verbose_province = _('Province')
verbose_city = _('City')
verbose_subdistrict = _('Subdistrict')
verbose_village = _('Village')
verbose_rw = _('RW')
verbose_rt = _('RT')


class EventAdmin(ImportExportModelAdmin,
                 ExportActionModelAdmin,
                 LeafletGeoAdmin):
    resource_class = EventResource

    # Leaflet widget override
    settings_overrides = {
        'DEFAULT_ZOOM': 11,
    }

    form = EventForm
    fieldsets = [
        (verbose_event_details, {
            'fields': [
                'created',
                'disaster',
                'status',
                'height',
                'magnitude',
                'note'
            ]
        }),
        (verbose_affected_area, {
            'fields': [
                'province',
                'city',
                'subdistrict',
                'village',
                'rw',
                'rt',
                'point'
            ],
            'classes': ['autocomplete-light-event']
        }),
    ]
    list_display = [
        'created',
        'updated',
        'status',
        'disaster',
        'province_admin_url',
        'city_admin_url',
        'subdistrict_admin_url',
        'village_admin_url',
        'rw_admin_url',
        'rt_admin_url',
        'height',
        'magnitude',
        'note'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['created', 'updated', 'status', 'disaster']
    search_fields = [
        'province__name',
        'city__name',
        'subdistrict__name',
        'village__name',
        'note'
    ]
    actions = [set_active, set_inactive]
    inlines = [ReportInline, EventImageInline, EventImpactInline]

    def import_action(self, request, *args, **kwargs):
        '''
        Overrides import_action() in import_export/admin.py
        just to pass a request object to import_data() to
        be used in before_import().
        '''
        resource = self.get_import_resource_class()()

        context = {}

        import_formats = self.get_import_formats()
        form = forms.ImportForm(import_formats,
                                request.POST or None,
                                request.FILES or None)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
            import_file = form.cleaned_data['import_file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            tmp_storage = self.get_tmp_storage_class()()
            data = bytes()
            for chunk in import_file.chunks():
                data += chunk

            tmp_storage.save(data, input_format.get_read_mode())

            # then read the file, using the proper format-specific mode
            # warning, big files may exceed memory
            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_text(data, self.from_encoding)
                dataset = input_format.create_dataset(data)
            except UnicodeDecodeError as e:
                return HttpResponse(_(u"<h1>Imported file is not in unicode: %s</h1>" % e))
            except Exception as e:
                return HttpResponse(_(u"<h1>%s encountred while trying to read file: %s</h1>" % (type(e).__name__, e)))
            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=False,
                                          file_name=import_file.name,
                                          user=request.user, request=request)

            context['result'] = result

            if not result.has_errors():
                context['confirm_form'] = forms.ConfirmImportForm(initial={
                    'import_file_name': tmp_storage.name,
                    'original_file_name': import_file.name,
                    'input_format': form.cleaned_data['input_format'],
                })

        if django.VERSION >= (1, 8, 0):
            context.update(self.admin_site.each_context(request))
        elif django.VERSION >= (1, 7, 0):
            context.update(self.admin_site.each_context())

        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_fields()]

        return TemplateResponse(request, [self.import_template_name],
                                context)

    def province_admin_url(self, obj):
        if not obj.province:
            return '-'
        return format_html(
            "<a href='{url}'>{province}</a>",
            url=obj.province.get_admin_url(),
            province=obj.province
        )

    province_admin_url.short_description = verbose_province

    def city_admin_url(self, obj):
        if not obj.city:
            return '-'
        return format_html(
            "<a href='{url}'>{city}</a>",
            url=obj.city.get_admin_url(),
            city=obj.city
        )

    city_admin_url.short_description = verbose_city

    def subdistrict_admin_url(self, obj):
        if not obj.subdistrict:
            return '-'
        return format_html(
            "<a href='{url}'>{subdistrict}</a>",
            url=obj.subdistrict.get_admin_url(),
            subdistrict=obj.subdistrict
        )

    subdistrict_admin_url.short_description = verbose_subdistrict

    def village_admin_url(self, obj):
        if not obj.village:
            return '-'
        return format_html(
            "<a href='{url}'>{village}</a>",
            url=obj.village.get_admin_url(),
            village=obj.village
        )

    village_admin_url.short_description = verbose_village

    def rw_admin_url(self, obj):
        if not obj.rw:
            return '-'
        return format_html(
            "<a href='{url}'>{rw}</a>",
            url=obj.rw.get_admin_url(),
            rw=obj.rw
        )

    rw_admin_url.short_description = verbose_rw

    def rt_admin_url(self, obj):
        if not obj.rt:
            return '-'
        return format_html(
            "<a href='{url}'>{rt}</a>",
            url=obj.rt.get_admin_url(),
            rt=obj.rt
        )

    rt_admin_url.short_description = verbose_rt


verbose_report_details = _('Report details')
verbose_event = _('Event')


class EventImageAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'image',
        'published'
    ]


verbose_impact_data = _('Impact data')


class EventImpactAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_ZOOM': 11,
    }

    form = EventImpactForm
    fieldsets = [
        (verbose_event, {
            'fields': [
                'event'
            ]
        }),
        (verbose_affected_area, {
            'fields': [
                'province',
                'city',
                'subdistrict',
                'village',
                'rw',
                'rt',
                'rt_text',
                'evac_point'
            ],
            'classes': ['autocomplete-light-eventimpact']
        }),
        (verbose_impact_data, {
            'fields': [
                ('affected_total', 'affected_death', 'affected_injury'),
                'evac_total',
                'loss_total',
                'note'
            ]
        }),
    ]
    list_display = [
        'event',
        'village',
        'rw',
        'rt',
        'rt_text',
        'affected_total',
        'affected_death',
        'affected_injury',
        'evac_total',
        'loss_total',
        'note'
    ]


class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_report_details, {
            'fields': [
                'created',
                'updated',
                'event',
                'source',
                'status',
                'note'
            ]
        })
    ]
    list_display = [
        'created',
        'updated',
        'event_admin_url',
        'source',
        'status',
        'note'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    list_filter = ['created', 'updated', 'source', 'status']
    search_fields = ['note']
    actions = [set_verified, set_unverified]

    def event_admin_url(self, obj):
        if not obj.event:
            return '-'
        return format_html(
            "<a href='{url}'>{event}</a>",
            url=obj.event.get_admin_url(),
            event=obj.event
        )

    event_admin_url.short_description = verbose_event


admin.site.register(Source, SourceAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventImage, EventImageAdmin)
admin.site.register(EventImpact, EventImpactAdmin)
