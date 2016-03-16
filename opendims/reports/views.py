from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from rest_framework import generics
from .serializers import EventSerializers, ReportSerializers

from .models import Event, Report


class EventListView(generic.ListView):
    queryset = Event.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class EventDetailView(generic.DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(event=self.get_object())
        return context


def report_list(request):
    reports = Report.objects.order_by('-created')
    context = {'reports': reports}
    return render(request, 'reports/report_list.html', context)


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {'report': report}
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
