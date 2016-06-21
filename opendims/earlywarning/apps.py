from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EarlywarningConfig(AppConfig):
    name = 'earlywarning'
    verbose_name = _('Early Warning')
