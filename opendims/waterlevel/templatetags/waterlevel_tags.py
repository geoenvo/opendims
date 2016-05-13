from django import template
import datetime

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
def get_watergate():
    watergates = WaterGate.objects.filter(
    ).order_by('name')
    return watergates
 
@register.simple_tag
def get_waterlevelreport_block(watergate):
    now = timezone.localtime(timezone.now())
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__date=(now.date())
    ).order_by('-created')
    return waterlevelreports 