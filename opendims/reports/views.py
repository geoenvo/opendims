from django.views import generic
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .serializers import EventSerializer, ReportSerializer
from rest_framework import filters

from common.views import CustomListAPIView
from .models import Event, Report, EventImpact, EventImage
from .filters import EventFilter, ReportFilter


def statistics(request):
    events = Event.objects.order_by('-created')
    eventimpacts = EventImpact.objects.order_by('-pk')
    context = {'events': events, 'eventimpacts': eventimpacts}

    total = 0
    for event in events:
        total = total + 1
    print total

    total_evac_value = 0
    total_affected_total = 0

    for eventimpact in eventimpacts:
        total_evac_value += eventimpact.evac_total
        total_affected_total += eventimpact.affected_total

    print total_evac_value
    print total_affected_total

    """if event.disaster.code == 'ABR':
            return sum(event.disaster.code)

        if event.disaster.code == 'BJR':
            return sum(event.disaster.code)
        else:
            print "I'm the others"""

    return render(request, 'reports/statistics.html', context)


class EventListView(generic.ListView):
    queryset = Event.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


def event_map(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event,
        }
    return render(request, 'reports/event_map.html', context)


def eventimpact_map(request, pk):
    event = get_object_or_404(Event, pk=pk)
    eventimpacts = EventImpact.objects.filter(event=event)
    context = {
        'eventimpacts': eventimpacts
    }
    return render(request, 'reports/eventimpact_map.html', context)


class EventDetailView(generic.DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(event=self.get_object())
        context['eventimpacts'] = EventImpact.objects.filter(event=self.get_object())
        context['eventimages'] = EventImage.objects.filter(event=self.get_object(), published=True).order_by('order')
        return context


class ReportListView(generic.ListView):
    queryset = Report.objects.filter(status='VERIFIED', event__isnull=False).order_by('-created')
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
