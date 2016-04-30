from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^eventassessment/$', views.EventAssessmentListView.as_view(), name='eventassessment_list'),
    url(r'^eventassessment/(?P<pk>\d+)/$', views.EventAssessmentDetailView.as_view(), name='eventassessment_detail'),
    url(r'^activity/$', views.ActivityListView.as_view(), name='activity_list'),
    url(r'^activity/(?P<pk>\d+)/$', views.ActivityDetailView.as_view(), name='activity_detail'),
]

urlpaterns = format_suffix_patterns(urlpatterns)
