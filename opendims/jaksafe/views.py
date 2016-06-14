import datetime

from django.shortcuts import render
from django.views import generic
from django.conf import settings
from django.utils import timezone

from rest_framework import generics, filters

from common.views import CustomListAPIView
from .models import ReportAutoSummary
from .filters import ReportAutoSummaryFilter
from .serializer import ReportAutoSummarySerializer


class ReportAutoSummaryListView(generic.ListView):
    queryset = ReportAutoSummary.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class ReportAutoSummaryDetailView(generic.DetailView):
    model = ReportAutoSummary


class APIReportAutoSummaryList(generics.ListAPIView):
    """
    Return JakSAFE auto summary reports on a given day based on the date
    parameter. If not returns the latest available report.
    JakSAFE auto summary reports are retrieved peridocally by cron from
    http://jaksafe.bpbd.jakarta.go.id/report/auto_report_json/.
    """
    serializer_class = ReportAutoSummarySerializer

    def get_queryset(self):
        date = self.request.query_params.get('date', None)
        queryset = ReportAutoSummary.objects.all()
        if date:
            try:
                date = timezone.make_aware(datetime.datetime.strptime(date, '%Y-%m-%d'))
                report_4_datetime = date.replace(hour=23)
                report_3_datetime = date.replace(hour=17)
                report_2_datetime = date.replace(hour=11)
                report_1_datetime = date.replace(hour=5)

                report_4 = queryset.filter(
                    created__year=report_4_datetime.year,
                    created__month=report_4_datetime.month,
                    created__day=report_4_datetime.day,
                    created__hour=report_4_datetime.hour
                )
                if report_4:  # ada laporan jam 23 di hari tersebut, return
                    return report_4
                    # jika di atas tidak ada, query untuk laporan 3
                report_3 = queryset.filter(
                    created__year=report_3_datetime.year,
                    created__month=report_3_datetime.month,
                    created__day=report_3_datetime.day,
                    created__hour=report_3_datetime.hour
                )
                if report_3:
                    return report_3

                report_2 = queryset.filter(
                    created__year=report_2_datetime.year,
                    created__month=report_2_datetime.month,
                    created__day=report_2_datetime.day,
                    created__hour=report_2_datetime.hour
                )
                if report_2:
                    return report_2

                report_1 = queryset.filter(
                    created__year=report_1_datetime.year,
                    created__month=report_1_datetime.month,
                    created__day=report_1_datetime.day,
                    created__hour=report_1_datetime.hour
                )
                if report_1:
                    return report_1
                else:
                    return queryset.none()
            except ValueError:
                    return queryset.none()
        else:
            # return report hari ini
            today = timezone.localtime(timezone.now())
            report_4_datetime = today.replace(hour=23)
            report_3_datetime = today.replace(hour=17)
            report_2_datetime = today.replace(hour=11)
            report_1_datetime = today.replace(hour=5)

            report_4 = queryset.filter(
                created__year=report_4_datetime.year,
                created__month=report_4_datetime.month,
                created__day=report_4_datetime.day,
                created__hour=report_4_datetime.hour
            )
            if report_4:  # ada laporan jam 23 di hari tersebut, return
                return report_4
                # jika di atas tidak ada, query untuk laporan 3
            report_3 = queryset.filter(
                created__year=report_3_datetime.year,
                created__month=report_3_datetime.month,
                created__day=report_3_datetime.day,
                created__hour=report_3_datetime.hour
            )
            if report_3:
                return report_3

            report_2 = queryset.filter(
                created__year=report_2_datetime.year,
                created__month=report_2_datetime.month,
                created__day=report_2_datetime.day,
                created__hour=report_2_datetime.hour
            )
            if report_2:
                return report_2

            report_1 = queryset.filter(
                created__year=report_1_datetime.year,
                created__month=report_1_datetime.month,
                created__day=report_1_datetime.day,
                created__hour=report_1_datetime.hour
            )
            if report_1:
                return report_1
            else:
                return queryset.none()
