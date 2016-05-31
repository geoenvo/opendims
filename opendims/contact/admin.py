from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'name',
        'website',
        'subject'
    ]
    ordering = ['-created']
    date_hierarchy = 'created'
    list_filter = ['created', 'subject']
    search_fields = ['subject', 'name', 'message']


admin.site.register(Contact, ContactAdmin)
