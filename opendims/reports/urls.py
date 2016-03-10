from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from reports import views

urlpatterns = [
    url(r'^event/$', views.event_list, name='event_list'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^report/$', views.report_list, name='report_list'),
    url(r'^report/(?P<pk>\d+)/$', views.report_detail, name='report_detail'),
    url(r'^api/$', views.EventList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^api2/$', views.ReportList.as_view()),
    url(r'^api2/(?P<pk>[0-9]+)/$', views.ReportDetail.as_view()),
]

urlpaterns = format_suffix_patterns(urlpatterns)
