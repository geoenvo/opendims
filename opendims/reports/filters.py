from rest_framework import filters
import django_filters

from .models import Event, Report


class EventFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    disaster = django_filters.CharFilter(
        name='disaster__code',
        lookup_expr='iexact'
    )

    class Meta:
        model = Event
        fields = ['id', 'disaster']


class ReportFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    disaster = django_filters.CharFilter(
        name='event__disaster__code',
        lookup_type='iexact'
    )
    source = django_filters.CharFilter(
        name='source__code',
        lookup_type='iexact'
    )

    class Meta:
        model = Report
        fields = ['id', 'disaster', 'source']
