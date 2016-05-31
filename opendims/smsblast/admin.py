from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import Template, Group, Message, Contact


class TemplateAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'created',
        'content'
    )
    list_display = [
        'name',
        'created',
        'updated'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created']
    search_fields = ['name', 'content']


class GroupAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'created',
        'contacts',
        'note'
    )
    list_display = [
        'name',
        'created',
        'updated'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created']
    search_fields = ['name', 'note']


class MessageAdmin(admin.ModelAdmin):
    fields = (
        'subject',
        'created',
        'template',
        'group',
        'content'
    )
    list_display = [
        'subject',
        'created',
        'updated',
        'group',
        'template'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created', 'group', 'template']
    search_fields = ['subject', 'group', 'template', 'content']


class ContactAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'created',
        'contact_number'
    )
    list_display = [
        'name',
        'created',
        'updated',
        'contact_number'
    ]
    readonly_fields = ['updated']
    ordering = ['-updated', '-created']
    date_hierarchy = 'created'
    list_filter = ['created']
    search_fields = ['name', 'contact_number']


admin.site.register(Template, TemplateAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Contact, ContactAdmin)
