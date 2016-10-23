from datetime import datetime
import cStringIO as StringIO 
import pdfkit

from django.shortcuts import render
from django.template.loader import get_template 
from django.template import Context
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse

from xhtml2pdf import pisa

from disasterrehabilitation.models import Activity, Agency
from reports.models import Event
from reporting.models import Report


def event_map(request):
    return render(request, 'maps/event_map.html')

def index(request):
    pdf = pdfkit.from_url('maps/event_map_new_pdf.html', False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hello.pdf"'
    return response

def event_map_new_pdf(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'maps/pdf_event_map.html', context)


def event_map_new(request):
    template = get_template('maps/event_map_new.html')
    events = Event.objects.all()
    date = datetime.now()
    events = events.filter(created__date=date)
    html = template.render({'events': events})
    pdf_map_temp = NamedTemporaryFile()
    pdf = pisa.pisaDocument(
        html.encode('utf-8'),
        dest=pdf_map_temp,
        encoding='utf-8'
    )
    event_lokasis = Event.objects.all()
    context = {'event_lokasis': event_lokasis}

    return render(request, 'maps/event_map_new.html', context)


def jaksafe_map(request):
    return render(request, 'maps/jaksafe_map.html')


def waterlevel_map(request):
    date = request.GET.get('date', None)
    return render(request, 'maps/waterlevel_map.html', {'date': date})


def rehabilitation_activity_map(request):
    """
    Show all activities if user is authenticated and all parameter is provided.
    By default only show published activities.
    Activities can be filtered by status/type/funding/agency.
    """
    all = request.GET.get('all', None)
    status = request.GET.get('status', None)
    type = request.GET.get('type', None)
    funding = request.GET.get('funding', None)
    agency = request.GET.get('agency', None)
    context = {}
    if all and request.user.is_authenticated():
        activities = Activity.objects.all()
    else:
        activities = Activity.objects.filter(published=True)
    if status:
        activities = activities.filter(status__iexact=status)
        context['status'] = status
    if type:
        activities = activities.filter(type__iexact=type)
        context['type'] = type
    if funding:
        activities = activities.filter(funding__iexact=funding)
        context['funding'] = funding
    if agency:
        activities = activities.filter(agency__pk=agency)
        context['selected_agency'] = agency
    agencies = Agency.objects.all().order_by("name")
    context['activities'] = activities
    context['agencies'] = agencies
    return render(request, 'maps/rehabilitation_activity_map.html', context)
