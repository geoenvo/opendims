from __future__ import unicode_literals

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
]

urlpaterns = format_suffix_patterns(urlpatterns)
