from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_screamshot/$', views.test_screamshot, name='test_screamshot')
]
