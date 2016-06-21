from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SmsblastConfig(AppConfig):
    name = 'smsblast'
    verbose_name = _('Sms Blast')
