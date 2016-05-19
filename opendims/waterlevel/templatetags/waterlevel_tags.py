from django import template
from django.utils import timezone

from waterlevel.models import WaterLevelReport, WaterGate

register = template.Library()


@register.simple_tag
def get_waterlevelreport(watergate, now):
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__date=(now.date())
    ).order_by('-created')
    return waterlevelreports


@register.simple_tag
def get_watergates():
    watergates = WaterGate.objects.all().order_by('name')
    return watergates


@register.simple_tag
def get_waterlevelreports_block(watergate):
    now = timezone.localtime(timezone.now())
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__date=(now.date())
    ).order_by('-created')
    return waterlevelreports
