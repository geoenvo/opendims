from __future__ import unicode_literals

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import Contact

verbose_Contact = _('Contact')


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'created',
        'name',
        'website',
        'subject'
    ]
    ordering = ['-created']
    list_filter = ['created']
    search_fields = ['message']

admin.site.register(Contact, ContactAdmin)
