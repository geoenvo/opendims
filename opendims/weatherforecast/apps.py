from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WeatherforecastConfig(AppConfig):
    name = 'weatherforecast'
    verbose_name = _('Weather Forecast')
