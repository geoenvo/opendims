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


admin.site.register(Template, TemplateAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Contact, ContactAdmin)
