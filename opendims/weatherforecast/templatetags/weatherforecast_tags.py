import datetime

from django import template
from django.utils import timezone
from weatherforecast.models import WeatherForecastReport

register = template.Library()


@register.simple_tag
def get_latest_weatherforecastreport_dki():
    now = timezone.localtime(timezone.now())
    weatherforecastreport = WeatherForecastReport.objects.filter(
        created__date=now.date(),
        province__id=31,
        city__isnull=True
    ).order_by('-created')[:1]
    return weatherforecastreport

        
@register.simple_tag
def get_latest_weatherforecastreport_by_city(city):
    now = timezone.localtime(timezone.now())
    weatherforecastreport = WeatherForecastReport.objects.filter(
        created__date=now.date(),
        province__isnull=True,
        city__id=city
    ).order_by('-created')[:1]
    return weatherforecastreport
    
    
   

    
    
