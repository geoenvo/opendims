from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^ReportAutoSummary/$', views.JaksafeReportAutoListView.as_view(), name='JaksafeReportAuto_list'),
    url(r'^ReportAutoSummary/(?P<pk>\d+)/$', views.JaksafeReportAutoDetailView.as_view(), name='JaksafeReportAuto_detail'),

]

urlpaterns = format_suffix_patterns(urlpatterns)
