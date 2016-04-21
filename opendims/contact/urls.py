from __future__ import unicode_literals

from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    url(r'^contact/$', views.ContactListView.as_view(), name='contact_list'),
    url(r'^contact/(?P<pk>\d+)/$', views.ContactDetailView.as_view(), name='contact_detail'),
    url(r'^contact/new/$', views.Contact_new, name='contact_new'),

]

urlpaterns = format_suffix_patterns(urlpatterns)
