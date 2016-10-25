from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WebsiteConfig(AppConfig):
    name = 'website'
    verbose_name = _('Website')
    def ready(self):
        import website.signals
        from actstream import registry
        registry.register(self.get_model('Verb'), self.get_model('Actor'), self.get_model('Object'))
