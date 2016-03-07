from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^autocomplete-province/$', views.AutocompleteProvince.as_view(), name='autocomplete_province'),
    url(r'^autocomplete-city/$', views.AutocompleteCity.as_view(), name='autocomplete_city'),
    url(r'^autocomplete-subdistrict/$', views.AutocompleteSubdistrict.as_view(), name='autocomplete_subdistrict'),
    url(r'^autocomplete-village/$', views.AutocompleteVillage.as_view(), name='autocomplete_village'),
    url(r'^province/$', views.province_list, name='province_list'),
    url(r'^province/(?P<pk>\d+)/$', views.province_detail, name='province_detail'),
    url(r'^city/(?P<pk>\d+)/$', views.city_detail, name='city_detail'),
    url(r'^subdistrict/(?P<pk>\d+)/$', views.subdistrict_detail, name='subdistrict_detail'),
    url(r'^village/(?P<pk>\d+)/$', views.village_detail, name='village_detail'),
    url(r'^rw/(?P<pk>\d+)/$', views.rw_detail, name='rw_detail'),
    url(r'^rt/(?P<pk>\d+)/$', views.rt_detail, name='rt_detail'),
]
