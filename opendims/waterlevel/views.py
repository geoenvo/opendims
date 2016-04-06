from django.shortcuts import render

from rest_framework import generics, filters

from .models import WaterGate
from .serializers import WaterLevelSerializer

































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
