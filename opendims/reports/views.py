from django.shortcuts import render, get_object_or_404
from .models import Event, Report


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