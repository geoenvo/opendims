from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GeolevelsConfig(AppConfig):
    name = 'geolevels'
    verbose_name = _('Geo Level')
