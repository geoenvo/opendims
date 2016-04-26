from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.contrib.gis import admin

from .models import Template, Group, Message, Contact

verbose_template_details = _('Template details')
verbose_group_details = _('Group details')
verbose_message_details = _('Message details')
verbose_contact_details = _('Contact details')
verbose_message_details = _('Message details')


class TemplateAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_template_details, {
            'fields': [
                'name',
                'created',
                'content'
            ]
        })
    ]
    list_display = [
        'name',
        'created',
        'updated'
    ]


class GroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_group_details, {
            'fields': [
                'name',
                'created',
                'contacts',
                'note'
            ]
        })
    ]
    list_display = [
        'name',
        'created',
        'updated'
    ]


class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_message_details, {
            'fields': [
                'subject',
                'created',
                'template',
                'group',
                'content'
            ]
        })
    ]
    list_display = [
        'subject',
        'created',
        'updated',
        'group',
        'template'
    ]


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (verbose_contact_details, {
            'fields': [
                'name',
                'created',
                'contact_number'
            ]
        })
    ]
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
