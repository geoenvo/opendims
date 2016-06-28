from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.views import generic
from django.conf import settings

from .models import AWSStation, AWSReport


class AWSStationListView(generic.ListView):
    queryset = AWSStation.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(AWSStationListView, self).get_context_data(**kwargs)
        return context


class AWSStationDetailView(generic.ListView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        self.awsstation = get_object_or_404(
            AWSStation,
            pk=pk
        )
        self.object_list = self.get_queryset()
        context = self.get_context_data(
            object_list=self.object_list,
            awsstation=self.awsstation
        )
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = AWSReport.objects.filter(awsstation=self.awsstation).order_by('-created')
        return queryset
