from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from .serializers import EventSerializer, ReportSerializer
from rest_framework import generics, filters

from common.views import CustomListAPIView
from .models import Event, Report
from .filters import EventFilter, ReportFilter


class EventListView(generic.ListView):
    queryset = Event.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class EventDetailView(generic.DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(event=self.get_object())
        return context


class ReportListView(generic.ListView):
    queryset = Report.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class ReportDetailView(generic.DetailView):
    model = Report

    def get_context_data(self, **kwargs):
        context = super(ReportDetailView, self).get_context_data(**kwargs)
        return context


class APIEventList(CustomListAPIView):
    queryset = Event.objects.filter(status='ACTIVE')
    serializer_class = EventSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = EventFilter
    ordering_fields = ('created',)
    ordering = ('-created',)


class APIReportList(CustomListAPIView):
    queryset = Report.objects.filter(status='VERIFIED')
    serializer_class = ReportSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = ReportFilter
    ordering_fields = ('created',)
    ordering = ('-created',)
