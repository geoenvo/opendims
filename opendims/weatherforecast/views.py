import datetime

from django.views import generic
from django.utils import timezone

from .models import WeatherForecastReport


class WeatherForecastReportListView(generic.ListView):
    def get(self, request, *args, **kwargs):
        self.date = request.GET.get('date', None)
        if self.date:
            try:
                self.date = timezone.make_aware(datetime.datetime.strptime(self.date, '%Y-%m-%d'))
            except:
                self.date = None
        self.object_list = self.get_queryset()
        context = self.get_context_data(
            object_list=self.object_list
        )
        if self.date:
            context['date'] = self.date.strftime('%d %B %Y')
        return self.render_to_response(context)

    def get_queryset(self):
        """
        Load weather forecast reports for a certain date. By default returns
        today's weather forecast. Accepts an optional date parameter in YYYY-MM-DD format.
        """
        today = timezone.localtime(timezone.now())
        queryset = WeatherForecastReport.objects.all().filter(created__date=today.date(), province__isnull=True)
        if self.date:
            queryset = WeatherForecastReport.objects.all().filter(created__date=self.date.date(), province__isnull=True)
        queryset = queryset.order_by('city__name')
        return queryset
