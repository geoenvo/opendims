from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(
        r'^api/$',
        views.APIWaterLevelList.as_view(),
        name='waterlevel_api'
    ),
    url(
        r'^waterlevelreport/$',
        views.WaterLevelReportListView.as_view(),
        name='waterlevelreport_list'
    ),
    url(
        r'^watergate/$',
        views.WaterGateListView.as_view(),
        name='watergate_list'
    ),


]

urlpaterns = format_suffix_patterns(urlpatterns)
