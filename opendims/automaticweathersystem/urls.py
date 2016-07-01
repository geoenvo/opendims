from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(
        r'^$',
        views.AWSStationListView.as_view(),
        name='awsstation_list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        views.AWSStationDetailView.as_view(),
        name='awsstation_detail'
    ),

]

urlpaterns = format_suffix_patterns(urlpatterns)
