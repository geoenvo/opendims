import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.conf import settings

from rest_framework import generics, filters

from .models import WaterGate, WaterLevelReport
from .serializers import WaterLevelSerializer


class WaterGateListView(generic.ListView):
    queryset = WaterGate.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(WaterGateListView, self).get_context_data(**kwargs)
        context['now'] = timezone.localtime(timezone.now())
        # Accept date parameter in YYYY-MM-DD format, date must be < now
        date = self.request.GET.get('date', None)
        if date:
            try:
                now = timezone.make_aware(datetime.datetime.strptime(date, '%Y-%m-%d'))
                if now.date() < context['now'].date():
                    context['now'] = now.replace(hour=23, minute=59, second=59)
            except:
                pass
        return context


class WaterGateDetailView(generic.ListView):
    paginate_by = settings.ITEMS_PER_PAGE
    template_name = 'waterlevel/watergate_detail.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.pop('pk', None)
        self.watergate = get_object_or_404(
            WaterGate,
            pk=pk
        )
        self.object_list = self.get_queryset()
        context = self.get_context_data(
            object_list=self.object_list,
            watergate=self.watergate
        )
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = WaterLevelReport.objects.filter(watergate=self.watergate).order_by('-created')
        return queryset


class APIWaterLevelList(generics.ListAPIView):
    """API for water level reports.
    Accepts date parameter in 'YYYY-MM-DD' format, if not provided
    returns the water level reports of the current day.
    """
    queryset = WaterGate.objects.all()
    serializer_class = WaterLevelSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
    ordering = ('name',)
