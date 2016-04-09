from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings
from django.utils import timezone

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
    serializer_class = EventSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = EventFilter
    ordering_fields = ('created',)
    ordering = ('-created',)

    def get_queryset(self):
        """
        For non authenticated users show ACTIVE events only.
        If 'date' parameter is not provided, return events from
        the current day only.
        If 'all' parameter is provided, show all records to
        authenticated users.
        """
        queryset = Event.objects.all()
        authenticated = self.request.user.is_authenticated()
        if not authenticated:
            queryset = queryset.filter(status='ACTIVE')
        date = self.request.query_params.get('date', None)
        show_all = self.request.query_params.get('all', None)
        if not date:
            if authenticated and show_all:
                return queryset
            now = timezone.localtime(timezone.now())
            queryset = queryset.filter(
                created__year=now.year,
                created__month=now.month,
                created__day=now.day
            )
        return queryset


class APIReportList(CustomListAPIView):
    serializer_class = ReportSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = ReportFilter
    ordering_fields = ('created',)
    ordering = ('-created',)

    def get_queryset(self):
        """
        For non authenticated users show VERIFIED reports only.
        If 'date' parameter is not provided, return reports from
        the current day only.
        If 'all' parameter is provided, show all records to
        authenticated users.
        """
        queryset = Report.objects.all()
        authenticated = self.request.user.is_authenticated()
        if not authenticated:
            queryset = queryset.filter(status='VERIFIED')
        date = self.request.query_params.get('date', None)
        show_all = self.request.query_params.get('all', None)
        if not date:
            if authenticated and show_all:
                return queryset
            now = timezone.localtime(timezone.now())
            queryset = queryset.filter(
                created__year=now.year,
                created__month=now.month,
                created__day=now.day
            )
        return queryset
