from django.shortcuts import render
from django.views import generic
from django.conf import settings

from rest_framework import generics

from reports.models import Event
from .forms import SearchByLocationForm
from .models import EventAssessment, Activity, Location, Reference
from .serializers import ActivityLocationSerializer


def disasterrehabilitation_index(request):
    events = Event.objects.order_by('-created')
    eventassessments = EventAssessment.objects.filter(published=True).order_by('-created')
    activities = Activity.objects.filter(published=True).order_by('-created')
    form = SearchByLocationForm(request.GET or None)

    context = {
        'events': events,
        'eventassessments': eventassessments,
        'activities': activities,
        'form': form,
        'search': False
    }

    if form.is_valid():
        province = form.cleaned_data.get('province', None)
        city = form.cleaned_data.get('city', None)
        subdistrict = form.cleaned_data.get('subdistrict', None)
        village = form.cleaned_data.get('village', None)
        rw = form.cleaned_data.get('rw', None)
        rt = form.cleaned_data.get('rt', None)

        locations = Location.objects.all()

        if province:
            events = events.filter(province=province)
            locations = locations.filter(province=province)
            eventassessments_id = []
            activities_id = []
            for location in locations:
                if location.eventassessment:
                    eventassessments_id.append(location.eventassessment.id)
                if location.activity:
                    activities_id.append(location.activity.id)
            eventassessments = eventassessments.filter(id__in=eventassessments_id)
            activities = activities.filter(id__in=activities_id)

        if city:
            events = events.filter(city=city)
            locations = locations.filter(city=city)
            eventassessments_id = []
            activities_id = []
            for location in locations:
                if location.eventassessment:
                    eventassessments_id.append(location.eventassessment.id)
                if location.activity:
                    activities_id.append(location.activity.id)
            eventassessments = eventassessments.filter(id__in=eventassessments_id)
            activities = activities.filter(id__in=activities_id)

        if subdistrict:
            events = events.filter(subdistrict=subdistrict)
            locations = locations.filter(subdistrict=subdistrict)
            eventassessments_id = []
            activities_id = []
            for location in locations:
                if location.eventassessment:
                    eventassessments_id.append(location.eventassessment.id)
                if location.activity:
                    activities_id.append(location.activity.id)
            eventassessments = eventassessments.filter(id__in=eventassessments_id)
            activities = activities.filter(id__in=activities_id)

        if village:
            events = events.filter(village=village)
            locations = locations.filter(village=village)
            eventassessments_id = []
            activities_id = []
            for location in locations:
                if location.eventassessment:
                    eventassessments_id.append(location.eventassessment.id)
                if location.activity:
                    activities_id.append(location.activity.id)
            eventassessments = eventassessments.filter(id__in=eventassessments_id)
            activities = activities.filter(id__in=activities_id)

        if rw:
            events = events.filter(rw=rw)
            locations = locations.filter(rw=rw)
            eventassessments_id = []
            activities_id = []
            for location in locations:
                if location.eventassessment:
                    eventassessments_id.append(location.eventassessment.id)
                if location.activity:
                    activities_id.append(location.activity.id)
            eventassessments = eventassessments.filter(id__in=eventassessments_id)
            activities = activities.filter(id__in=activities_id)

        if rt:
            events = events.filter(rt)
            locations = locations.filter(rt)
            eventassessments_id = []
            activities_id = []
            for location in locations:
                if location.eventassessment:
                    eventassessments_id.append(location.eventassessment.id)
                if location.activity:
                    activities_id.append(location.activity.id)
            eventassessments = eventassessments.filter(id__in=eventassessments_id)
            activities = activities.filter(id__in=activities_id)

        context['search'] = True
        context['events'] = events
        context['eventassessments'] = eventassessments
        context['activities'] = activities

    return render(
        request,
        'disasterrehabilitation/disasterrehabilitation_index.html',
        context
    )


class EventAssessmentListView(generic.ListView):
    queryset = EventAssessment.objects.filter(published=True).order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class EventAssessmentDetailView(generic.DetailView):
    model = EventAssessment

    def get_context_data(self, **kwargs):
        context = super(EventAssessmentDetailView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.filter(
            eventassessment=self.get_object()
        )
        return context


class ActivityListView(generic.ListView):
    queryset = Activity.objects.filter(published=True).order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class ActivityDetailView(generic.DetailView):
    model = Activity

    def get_context_data(self, **kwargs):
        context = super(ActivityDetailView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.filter(
            activity=self.get_object()
        )
        context['references'] = Reference.objects.filter(
            activity=self.get_object(),
            published=True
        )
        return context


class APIActivityLocationList(generics.ListAPIView):
    serializer_class = ActivityLocationSerializer

    def get_queryset(self):
        """
        Show only published activity to non authenticated users.
        """
        authenticated = self.request.user.is_authenticated()
        id = self.request.query_params.get('id', None)
        if not id.isnumeric():
            id = None
        activity = Activity.objects.filter(pk=id)
        if activity and not authenticated:
            activity = activity.filter(published=True)
        if activity:
            queryset = Location.objects.filter(activity=activity[0])
            return queryset
        return Location.objects.none()
