from django.shortcuts import render, get_object_or_404
from reports.models import Event, Report


# Create your views here.
def event_list(request):
	event = Event.objects.all()
	return render (request, 'reports/event_list.html',{'event': event})


def event_detail(request, id):
    id = int(id)
    event = get_object_or_404(Event, id=id)
    return render(request,
                  "reports/event_detail.html",
                  {'event': event}
                  )