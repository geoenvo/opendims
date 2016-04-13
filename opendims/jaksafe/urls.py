from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^reportautosummary/$', views.ReportAutoSummaryListView.as_view(), name='reportautosummary_list'),
    url(r'^reportautosummary/(?P<pk>\d+)/$', views.ReportAutoSummaryDetailView.as_view(), name='reportautosummary_detail'),
    url(r'^reportautosummary/api/$', views.APIReportAutoSummaryList.as_view(), name='APIReportAutoSummaryList'),
]

urlpaterns = format_suffix_patterns(urlpatterns)
