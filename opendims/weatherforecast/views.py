import datetime

from django.views import generic
from django.utils import timezone

from .models import WeatherForecastReport


class WeatherForecastReportListView(generic.ListView):
    def get_queryset(self):
        """
        Load weather forecast reports for a certain date. By default returns
        today's weather forecast. Accepts an optional date parameter in YYYY-MM-DD format.
        """
        today = timezone.localtime(timezone.now())
        queryset = WeatherForecastReport.objects.all().filter(created__date=today.date(), province__isnull=True)
        date = self.request.GET.get('date', None)
        if date:
            try:
                date = timezone.make_aware(datetime.datetime.strptime(date, '%Y-%m-%d'))
                queryset = WeatherForecastReport.objects.all().filter(created__date=date.date(), province__isnull=True)
            except:
                pass
        queryset = queryset.order_by('city__name')
        return queryset
