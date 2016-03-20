from rest_framework import filters
import django_filters

from .models import Province, City, Subdistrict, Village, RW, RT


class ProvinceFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    id = django_filters.NumberFilter(name='id', lookup_type='exact')

    class Meta:
        model = Province
        fields = ['id', 'name']


class CityFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    id = django_filters.NumberFilter(name='id', lookup_type='exact')
    province = django_filters.CharFilter(name='province__name', lookup_type='iexact')

    class Meta:
        model = City
        fields = ['id', 'province', 'name']


class SubdistrictFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    id = django_filters.NumberFilter(name='id', lookup_type='exact')
    city = django_filters.CharFilter(name='city__name', lookup_type='iexact')

    class Meta:
        model = Subdistrict
        fields = ['id', 'city', 'name']


class VillageFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    id = django_filters.NumberFilter(name='id', lookup_type='exact')
    subdistrict = django_filters.CharFilter(name='subdistrict__name', lookup_type='iexact')

    class Meta:
        model = Village
        fields = ['id', 'subdistrict', 'name']


class RWFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    id = django_filters.NumberFilter(name='id', lookup_type='exact')
    village = django_filters.CharFilter(name='village__name', lookup_type='iexact')

    class Meta:
        model = RW
        fields = ['id', 'village', 'name']


class RTFilter(filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    id = django_filters.NumberFilter(name='id', lookup_type='exact')
    rw = django_filters.CharFilter(name='rw__name', lookup_type='iexact')

    class Meta:
        model = RT
        fields = ['id', 'rw', 'name']
