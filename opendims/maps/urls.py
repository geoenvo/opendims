from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event/$', views.event_map, name='event_map'),
    url(r'^event_map_new/$', views.event_map_new, name='event_map_new'),
    url(r'^waterlevel/$', views.waterlevel_map, name='waterlevel_map'),
    url(r'^aws/$', views.sensor_map, name='sensor_map'),
    url(r'^report_auto_summary/$', views.jaksafe_map, name='jaksafe_map'),
    url(r'^rehabilitation_activity/$', views.rehabilitation_activity_map, name='rehabilitation_activity_map'),
    url(r'^event_map_new_pdf/$', views.event_map_new_pdf, name='event_map_new_pdf'),
    # url(r'^index/$', views.index, name='index'),
    ]

