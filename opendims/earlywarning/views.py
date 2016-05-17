from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from .models import EarlyWarningReport


class EarlyWarningReportListView(generic.ListView):
    queryset = EarlyWarningReport.objects.filter(published=True).order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class EarlyWarningReportDetailView(generic.DetailView):
    model = EarlyWarningReport
