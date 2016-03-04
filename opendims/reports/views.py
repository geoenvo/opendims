from django.shortcuts import render, get_object_or_404
from .models import Event, Report


def event_list(request):
	events = Event.objects.all()
	context = {'events': events}
	return render(request, 'reports/event_list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reports = Report.objects.filter(event=event)
    context = {'event': event, 'reports': reports}
    return render(request, 'reports/event_detail.html', context)