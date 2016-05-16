from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from .models import EarlyWarningReport


class EarlyWarningReportListView(generic.ListView):
    paginate_by = settings.ITEMS_PER_PAGE
    queryset = EarlyWarningReport.objects.all().order_by('-created')


class EarlyWarningReportDetailView(generic.DetailView):
    model = EarlyWarningReport

    def get_context_data(self, **kwargs):
        context = super(EarlyWarningReportDetailView, self).get_context_data(**kwargs)
        return context
