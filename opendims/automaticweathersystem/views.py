from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views import generic
from django.conf import settings

from .models import SensorStation, SensorReport


class SensorStationListView(generic.ListView):
    queryset = SensorStation.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(SensorStationListView, self).get_context_data(**kwargs)
        return context


class SensorStationDetailView(generic.ListView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        self.sensorstation = get_object_or_404(
            SensorStation,
            pk=pk
        )
        self.object_list = self.get_queryset()
        context = self.get_context_data(
            object_list=self.object_list,
            sensorstation=self.sensorstation
        )
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = SensorReport.objects.filter(sensorstation=self.sensorstation).order_by('-created')
        return queryset
