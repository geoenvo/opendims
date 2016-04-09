from django.views import generic
from django.conf import settings

from .serializers import EventSerializer, ReportSerializer
from rest_framework import filters

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
        Show ACTIVE events only to non authenticated users.
        If 'all' parameter is provided, show all events to
        authenticated users.
        """
        authenticated = self.request.user.is_authenticated()
        all = self.request.query_params.get('all', None)
        queryset = Event.objects.all()
        if authenticated and all == '1':
            return queryset
        else:
            return queryset.filter(status='ACTIVE')


class APIReportList(CustomListAPIView):
    serializer_class = ReportSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = ReportFilter
    ordering_fields = ('created',)
    ordering = ('-created',)

    def get_queryset(self):
        """
        Show VERIFIED reports only to non authenticated users.
        If 'all' parameter is provided, show all reports to
        authenticated users.
        """
        authenticated = self.request.user.is_authenticated()
        all = self.request.query_params.get('all', None)
        queryset = Report.objects.all()
        if authenticated and all == '1':
            return queryset
        else:
            return queryset.filter(status='VERIFIED')
