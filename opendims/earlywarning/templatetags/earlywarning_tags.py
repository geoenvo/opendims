import datetime

from django import template
from django.utils import timezone
from earlywarning.models import EarlyWarningReport

register = template.Library()


@register.simple_tag
def get_latest_earlywarningreports():
    earlywarningreports = EarlyWarningReport.objects.all(
    ).order_by('-created')[:5]
    return earlywarningreports