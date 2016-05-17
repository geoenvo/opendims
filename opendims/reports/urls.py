from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^event/$', views.EventListView.as_view(), name='event_list'),
    url(r'^event_map/(?P<pk>\d+)/$', views.event_map, name='event_map'),
    url(
        r'^eventimpact_map/(?P<pk>\d+)/$',
        views.eventimpact_map,
        name='eventimpact_map'),
    url(
        r'^event/(?P<pk>\d+)/$',
        views.EventDetailView.as_view(),
        name='event_detail'
    ),
    url(r'^report/$', views.ReportListView.as_view(), name='report_list'),
    url(
        r'^report/(?P<pk>\d+)/$',
        views.ReportDetailView.as_view(),
        name='report_detail'
    ),
    url(r'^event/statistics/$', views.statistics, name='statistics'),
    url(r'^event/api/$', views.APIEventList.as_view(), name='event_api'),
    url(r'^report/api/$', views.APIReportList.as_view(), name='report_api'),
]

urlpaterns = format_suffix_patterns(urlpatterns)
