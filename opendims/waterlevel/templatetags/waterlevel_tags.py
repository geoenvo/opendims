import datetime

from django import template
from django.utils import timezone
from waterlevel.models import WaterLevelReport

register = template.Library()


@register.simple_tag
def get_waterlevelreport(watergate, now):
    date_start = datetime.datetime(now.year, now.month, now.day, 0)
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__range=(date_start, now)
    ).order_by('created')
    return waterlevelreports