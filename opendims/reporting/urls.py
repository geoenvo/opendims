from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_screamshot/$', views.test_screamshot, name='test_screamshot')
]

urlpatterns = [
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^weather_forecast/$', views.weather_forecast, name='weather_forecast'),
    url(r'^waterlevel/$', views.waterlevel, name='waterlevel'),
    url(r'^report_ABR/$', views.report_ABR, name='report_ABR')

]
