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
        city__name__iexact=city
    ).order_by('-created')[:1]
    return weatherforecastreport

    
@register.simple_tag
def get_latest_weatherforecastreport():
    now = timezone.localtime(timezone.now())
    weatherforecastreports = WeatherForecastReport.objects.filter(
        created__date=now.date(),
        province__isnull=True
    ).order_by('-created')
    return weatherforecastreports

    
@register.simple_tag
def get_forecast_details(forecast):
    forecast_details = {}
    forecast_text = ''
    weather_icon_class = ''
    if forecast == 'CERAH':
        forecast_text = 'Clear'
        weather_icon_class = 'wi-day-sunny'
    elif forecast == 'CERAH BERAWAN':
        forecast_text = 'Partly cloudy'
        weather_icon_class = 'wi-day-sunny-overcast'
    elif forecast == 'BERAWAN':
        forecast_text = 'Cloudy'
        weather_icon_class = 'wi-cloudy'
    elif forecast == 'HUJAN RINGAN':
        forecast_text = 'Light rain'
        weather_icon_class = 'wi-sprinkle'
    elif forecast == 'HUJAN SEDANG':
        forecast_text = 'Moderate rain'
        weather_icon_class = 'wi-showers'
    elif forecast == 'HUJAN DERAS':
        forecast_text = 'Heavy rain'
        weather_icon_class = 'wi-rain'
    forecast_details['forecast_text'] = forecast_text
    forecast_details['weather_icon_class'] = weather_icon_class
    return forecast_details
