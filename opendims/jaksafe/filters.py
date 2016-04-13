from rest_framework import filters
import django_filters

from .models import ReportAutoSummary


class ReportAutoSummaryFilter(filters.FilterSet):

    date = django_filters.DateFilter(name='created', lookup_expr='contains')

    class Meta:
        model = ReportAutoSummary
        fields = ['date']
