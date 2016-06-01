from django.shortcuts import render

from disasterrehabilitation.models import Activity, Agency


def event_map(request):
    return render(request, 'maps/event_map.html')


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
