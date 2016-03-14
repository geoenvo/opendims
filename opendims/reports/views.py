from django.shortcuts import render, get_object_or_404
from .models import Event, Report

from rest_framework import generics
from .serializers import EventSerializers, ReportSerializers


def event_list(request):
    events = Event.objects.order_by('-created')
    context = {'events': events}
    return render(request, 'reports/event_list.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reports = event.report_set.order_by('-created')
    context = {'event': event, 'reports': reports}
    return render(request, 'reports/event_detail.html', context)


def report_list(request):
    reports = Report.objects.order_by('-created')
    context = {'reports': reports}
    return render(request, 'reports/report_list.html', context)


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {'report': report}
    return render(request, 'reports/report_detail.html', context)


class APIEventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers


class APIEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers


class APIReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


class APIReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers
