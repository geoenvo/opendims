from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings
from django.utils import timezone

from rest_framework import generics, filters

from .models import WaterGate, WaterLevelReport
from .serializers import WaterLevelSerializer


class WaterGateListView(generic.ListView):
    queryset = WaterGate.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super(WaterGateListView, self).get_context_data(**kwargs)
        context['now'] = timezone.localtime(timezone.now())
        return context


class WaterGateDetailView(generic.DetailView):
    model = WaterGate

    def get_context_data(self, **kwargs):
        context = super(WaterGateDetailView, self).get_context_data(**kwargs)
        context['waterlevelreports'] = WaterLevelReport.objects.filter(watergate=self.get_object())
        return context


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
