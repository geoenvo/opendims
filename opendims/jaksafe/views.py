from django.shortcuts import render
from django.views import generic
from django.conf import settings

from rest_framework import generics, filters

from common.views import CustomListCreateAPIView
from .models import JaksafeReportAuto

class JaksafeReportAutoListView(generic.ListView):
    queryset = JaksafeReportAuto.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE

class JaksafeReportAutoDetailView(generic.DetailView):
    model = JaksafeReportAuto
