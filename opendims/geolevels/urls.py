from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^autocomplete-province/$', views.AutocompleteProvince.as_view(), name='autocomplete_province'),
    url(r'^autocomplete-city/$', views.AutocompleteCity.as_view(), name='autocomplete_city'),
    url(r'^autocomplete-subdistrict/$', views.AutocompleteSubdistrict.as_view(), name='autocomplete_subdistrict'),
    url(r'^autocomplete-village/$', views.AutocompleteVillage.as_view(), name='autocomplete_village'),
    url(r'^autocomplete-rw/$', views.AutocompleteRW.as_view(), name='autocomplete_rw'),
    url(r'^autocomplete-rt/$', views.AutocompleteRT.as_view(), name='autocomplete_rt'),
    url(r'^province/$', views.ProvinceListView.as_view(), name='province_list'),
    url(
        r'^province/(?P<pk>\d+)/$',
        views.ProvinceDetailView.as_view(),
        name='province_detail'
    ),
    url(r'^province/api/$', views.APIProvinceList.as_view(), name='province_api'),
    url(r'^city/$', views.CityListView.as_view(), name='city_list'),
    url(
        r'^city/(?P<pk>\d+)/$',
        views.CityDetailView.as_view(),
        name='city_detail'
    ),
    url(r'^city/api/$', views.APICityList.as_view(), name='city_api'),
    url(r'^subdistrict/$', views.SubdistrictListView.as_view(), name='subdistrict_list'),
    url(
        r'^subdistrict/(?P<pk>\d+)/$',
        views.SubdistrictDetailView.as_view(),
        name='subdistrict_detail'
    ),
    url(r'^subdistrict/api/$', views.APISubdistrictList.as_view(), name='subdistrict_api'),
    url(r'^village/$', views.VillageListView.as_view(), name='village_list'),
    url(
        r'^village/(?P<pk>\d+)/$',
        views.VillageDetailView.as_view(),
        name='village_detail'
        ),
    url(r'^village/api/$', views.APIVillageList.as_view(), name='village_api'),
    url(r'^rw/$', views.RWListView.as_view(), name='rw_list'),
    url(
        r'^rw/(?P<pk>\d+)/$',
        views.RWDetailView.as_view(),
        name='rw_detail'
        ),
    url(r'^rw/api/$', views.APIRWList.as_view(), name='rw_api'),
    url(r'^rt/$', views.VillageListView.as_view(), name='rt_list'),
    url(
        r'^rt/(?P<pk>\d+)/$',
        views.RTDetailView.as_view(),
        name='rt_detail'
        ),
    url(r'^rt/api/$', views.APIRTList.as_view(), name='rt_api'),
]
