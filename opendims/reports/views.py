from django.shortcuts import render, get_object_or_404
from .models import Event, Report
from rest_framework import generics
from .serializers import EventSerializers, ReportSerializers


def event_list(request):
    events = Event.objects.all().order_by('-created')
    context = {'events': events}
    return render(request, 'reports/event_list.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reports = Report.objects.filter(event=event).order_by('-created')
    context = {'event': event, 'reports': reports}
    return render(request, 'reports/event_detail.html', context)


def report_list(request):
    reports = Report.objects.all().order_by('-created')
    context = {'reports': reports}
    return render(request, 'reports/report_list.html', context)


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    event = Event.objects.get(pk=report.event.pk)
    context = {'report': report, 'event': event}
    return render(request, 'reports/report_detail.html', context)


class APIEventList(generics.ListCreateAPIView):
        queryset = Event.objects.filter(status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterABR(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='ABR', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterBJR(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='BJR', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterCEK(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='CEK', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterGMP(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='GMP', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterKBK(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='KBK', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterLAI(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='LAI', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterLSR(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='LSR', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterROB(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='ROB', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterSOS(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='SOS', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterTER(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='TER', status='ACTIVE')
        serializer_class = EventSerializers


class APIDisasterTSU(generics.ListCreateAPIView):
        queryset = Event.objects.filter(disaster='TSU', status='ACTIVE')
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
