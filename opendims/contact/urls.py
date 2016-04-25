from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^$', views.Contact_new, name='contact_new'),

]

urlpaterns = format_suffix_patterns(urlpatterns)
