from django.shortcuts import render
from django.views import generic
from django.conf import settings

from .models import Activity, Location, Reference


class ActivityListView(generic.ListView):
    queryset = Activity.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class ActivityDetailView(generic.DetailView):
    model = Activity

    def get_context_data(self, **kwargs):
        context = super(ActivityDetailView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.filter(activity=self.get_object())
        context['references'] = Reference.objects.filter(activity=self.get_object(), published=True)
        return context
