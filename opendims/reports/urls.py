from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^event/$', views.event_list, name='event_list'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^report/$', views.report_list, name='report_list'),
    url(r'^report/(?P<pk>\d+)/$', views.report_detail, name='report_detail'),
    url(r'^event/api/$', views.APIEventList.as_view()),
    url(r'^event/(?P<pk>\d+)/api/$', views.APIEventDetail.as_view()),
    url(r'^event/ABR/api/$', views.APIDisasterABR.as_view()),
    url(r'^event/BJR/api/$', views.APIDisasterBJR.as_view()),
    url(r'^event/CEK/api/$', views.APIDisasterCEK.as_view()),
    url(r'^event/GMP/api/$', views.APIDisasterGMP.as_view()),
    url(r'^event/KBK/api/$', views.APIDisasterKBK.as_view()),
    url(r'^event/LAI/api/$', views.APIDisasterLAI.as_view()),
    url(r'^event/LSR/api/$', views.APIDisasterLSR.as_view()),
    url(r'^event/ROB/api/$', views.APIDisasterROB.as_view()),
    url(r'^event/SOS/api/$', views.APIDisasterSOS.as_view()),
    url(r'^event/TER/api/$', views.APIDisasterTER.as_view()),
    url(r'^event/TSU/api/$', views.APIDisasterTSU.as_view()),
    url(r'^report/api/$', views.APIReportList.as_view()),
    url(r'^report/(?P<pk>\d+)/api/$', views.APIReportDetail.as_view()),
]

urlpaterns = format_suffix_patterns(urlpatterns)
