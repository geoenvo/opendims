from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportingConfig(AppConfig):
    name = 'reporting'
    verbose_name = _('Pusdalops Reporting')
