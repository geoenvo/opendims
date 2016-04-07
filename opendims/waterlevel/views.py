from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from rest_framework import generics, filters

from .models import WaterGate, WaterLevelReport
from .serializers import WaterLevelSerializer


class WaterLevelReportListView(generic.ListView):
    queryset = WaterLevelReport.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE

class WaterGateListView(generic.ListView):
    queryset = WaterGate.objects.order_by('-name')
    paginate_by = settings.ITEMS_PER_PAGE


"""
class EventDetailView(generic.DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(event=self.get_object())
        return context


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {'report': report}
    return render(request, 'reports/report_detail.html', context)
"""


def waterlevelreport_list(request):
    waterlevelreports = WaterLevelReport.objects.order_by('-created')
    context = {'waterlevelreports': waterlevelreports}
    return render(request, 'waterlevelreports/waterlevelreport_list.html', context)


def watergate_list(request):
    watergates = WaterGate.objects.order_by('-name')
    context = {'watergates': watergates}
    return render(request, 'watergate/watergate_list.html', context)




























class APIWaterLevelList(generics.ListAPIView):
    """API for water level reports.

    Accepts date parameter in 'YYYY-MM-DD' format, if not provided
    returns the water level reports of the current day.
    """
    queryset = WaterGate.objects.all()
    serializer_class = WaterLevelSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
    ordering = ('name',)
