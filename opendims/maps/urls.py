from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [url(r'^event/$', views.event_map, name='event_map'), ]