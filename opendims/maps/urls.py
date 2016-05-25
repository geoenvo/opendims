from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event/$', views.event_map, name='event_map'),
    url(r'^waterlevel/$', views.waterlevel_map, name='waterlevel_map'),
    url(r'^report_auto_summary/$', views.jaksafe_map, name='jaksafe_map'),
    url(r'^rehabilitation_activity/$', views.rehabilitation_activity_map, name='rehabilitation_activity_map'),
    ]
