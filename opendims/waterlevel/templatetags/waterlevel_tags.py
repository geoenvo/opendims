from django import template

from waterlevel.models import WaterLevelReport

register = template.Library()


@register.simple_tag
def get_waterlevelreport(watergate, now):
    waterlevelreports = WaterLevelReport.objects.filter(
        watergate=watergate,
        created__date=(now.date())
    ).order_by('created')
    return waterlevelreports
