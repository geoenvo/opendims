from rest_framework import filters
import django_filters

from .models import Event


class EventFilter(filters.FilterSet):
    disaster = django_filters.CharFilter(
        name='disaster__code',
        lookup_expr='iexact'
    )

    class Meta:
        model = Event
        fields = ['disaster']
