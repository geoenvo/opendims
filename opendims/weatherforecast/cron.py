import urllib2
import xml.etree.ElementTree as ET
import datetime

from django.utils import timezone

from .models import WeatherForecastReport
from geolevels.models import City, Province


def weatherforecast_scheduled_job():
    """
    Cron job for gathering weather forecast from BMKG.
    Run job before midnight to gather tomorrow's weather forecast.
    """
    # Available forecast for today+1
    today = timezone.localtime(timezone.now())
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)

    # Weather forecast for Jabodetabek cities
    path_city = urllib2.urlopen('http://data.bmkg.go.id/cuaca_jabodetabek_2.xml')
    tree_city = ET.parse(path_city)
    root_city = tree_city.getroot()
    data_city = root_city.findall('*//Row')

    for forecast_city in data_city:
        city = forecast_city.find('Daerah').text.upper()
        morning = forecast_city.find('Pagi').text.upper()
        noon = forecast_city.find('Siang').text.upper()
        night = forecast_city.find('Malam').text.upper()
        weather_forecast_city = WeatherForecastReport(
            created=tomorrow,
            city=City.objects.get(name=city),
            forecast_morning=morning,
            forecast_noon=noon,
            forecast_night=night
        )
        weather_forecast_city.save()

    # Weather forecast for DKI Jakarta province
    path_province = urllib2.urlopen('http://data.bmkg.go.id/cuaca_indo_2.xml')
    tree_province = ET.parse(path_province)
    root_province = tree_province.getroot()
    data_province = root_province.findall('*//Row')

    for forecast_province in data_province:
        province = forecast_province.find('Kota').text.upper()
        if province == 'JAKARTA':
            forecast = forecast_province.find('Cuaca').text.upper()
            temperature_min = forecast_province.find('SuhuMin').text.upper()
            temperature_max = forecast_province.find('SuhuMax').text.upper()
            humidity_min = forecast_province.find('KelembapanMin').text.upper()
            humidity_max = forecast_province.find('KelembapanMax').text.upper()
            weather_forecast_province = WeatherForecastReport(
                created=tomorrow,
                province=Province.objects.get(id=31),
                forecast=forecast,
                temperature_min=temperature_min,
                temperature_max=temperature_max,
                humidity_min=humidity_min,
                humidity_max=humidity_max
            )
            weather_forecast_province.save()
