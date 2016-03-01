
from djgeojson.views import GeoJSONLayerView
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event/$', views.event_list, name='event_list'),
    url(r'^event/(?P<id>\d+)/$', views.event_detail, name='event_detail'),


]
