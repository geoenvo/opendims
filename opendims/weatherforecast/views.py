from django.views import generic
from django.conf import settings

from .models import WeatherForecastReport


class WeatherForecastReportListView(generic.ListView):
    queryset = WeatherForecastReport.objects.all().order_by('city__name')
