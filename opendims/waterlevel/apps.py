from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WaterlevelConfig(AppConfig):
    name = 'waterlevel'
    verbose_name = _('Water Level')
