from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import Source, Keyword


verbose_source_details = _('Source details')


class KeywordInline(admin.TabularInline):
    model = Keyword
    extra = 3


class SourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_source_details, {
            'fields': [
                'name',
                'created',
                'type',
                'disaster',
                'status'
            ]
        })
    ]
    list_display = [
        'name',
        'created',
        'updated',
        'type',
        'disaster',
        'status'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created', 'type', 'disaster', 'status']
    search_fields = ['name', 'disaster', 'type']
    inlines = [KeywordInline]


class KeywordAdmin(admin.ModelAdmin):
    fields = (
        'source',
        'keyword'
    )
    list_display = [
        'source',
        'keyword'
    ]
    list_filter = ['source__name']
    search_fields = ['keyword', 'source__name']


admin.site.register(Source, SourceAdmin)
admin.site.register(Keyword, KeywordAdmin)
