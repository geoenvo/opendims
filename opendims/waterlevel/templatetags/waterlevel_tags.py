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


@register.simple_tag
def get_waterlevelreport_old(watergate, hour):
    now = timezone.localtime(timezone.now())
    created = datetime.datetime(now.year, now.month, now.day, hour)
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__year=created.year,
        created__month=created.month,
        created__day=created.day,
        created__hour=created.hour
    ).order_by('-created')

    if waterlevelreports:
        return waterlevelreports[0]
    else:
        return False


@register.simple_tag
def get_waterlevelreportchart(watergate, hour):
    now = timezone.localtime(timezone.now())
    created = datetime.datetime(now.year, now.month, now.day, hour)
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__year=created.year,
        created__month=created.month,
        created__day=created.day,
        created__hour=created.hour
    ).order_by('-created')

    if waterlevelreports:
        return waterlevelreports[0].height
    else:
        return '0'
