from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import Source, Keyword


verbose_source_details = _('Source details')
verbose_keyword_details = _('Keyword details')


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
    inlines = [KeywordInline]


class KeywordAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_keyword_details, {
            'fields': [
                'source',
                'keyword'
            ]
        })
    ]
    list_display = [
        'source',
        'keyword'
    ]

    search_fields = ['keyword']


admin.site.register(Source, SourceAdmin)
admin.site.register(Keyword, KeywordAdmin)
