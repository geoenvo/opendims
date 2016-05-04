from django import template

from earlywarning.models import EarlyWarningReport

register = template.Library()


@register.simple_tag
def get_earlywarningreports():
    earlywarningreports = EarlyWarningReport.objects.filter(
        published=True
    ).order_by('-created')
    return earlywarningreports
