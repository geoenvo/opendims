from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(
        r'^api/$',
        views.APISensorStationList.as_view(),
        name='sensor_api'
    ),
    url(
        r'^$',
        views.SensorStationListView.as_view(),
        name='sensorstation_list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        views.SensorStationDetailView.as_view(),
        name='sensorstation_detail'
    ),

]

urlpaterns = format_suffix_patterns(urlpatterns)
