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
]

urlpaterns = format_suffix_patterns(urlpatterns)
