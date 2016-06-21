from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportaggregatorConfig(AppConfig):
    name = 'reportaggregator'
    verbose_name = _('Report Aggregator')
