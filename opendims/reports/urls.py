from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^event/$', views.EventListView.as_view(), name='event_list'),
    url(
        r'^event/(?P<pk>\d+)/$',
        views.EventDetailView.as_view(),
        name='event_detail'
    ),
    url(r'^report/$', views.report_list, name='report_list'),
    url(r'^report/(?P<pk>\d+)/$', views.report_detail, name='report_detail'),
    url(r'^event/api/$', views.APIEventList.as_view(), name='event_api'),
    url(r'^report/api/$', views.APIReportList.as_view()),
    url(r'^report/(?P<pk>\d+)/api/$', views.APIReportDetail.as_view()),
]

urlpaterns = format_suffix_patterns(urlpatterns)
