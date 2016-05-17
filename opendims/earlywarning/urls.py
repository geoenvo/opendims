from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(
        r'^$',
        views.EarlyWarningReportListView.as_view(),
        name='earlywarningreport_list'
        ),
    url(
        r'^(?P<pk>\d+)/$',
        views.EarlyWarningReportDetailView.as_view(),
        name='earlywarningreport_detail'
    ),
]

urlpaterns = format_suffix_patterns(urlpatterns)
