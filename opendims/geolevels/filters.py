from rest_framework import filters
import django_filters

from .models import Province, City, Subdistrict, Village, RW, RT


class ProvinceFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    name = django_filters.CharFilter(name='name', lookup_type='iexact')

    class Meta:
        model = Province
        fields = ['id', 'name']


class CityFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    province = django_filters.CharFilter(
        name='province__name',
        lookup_type='iexact'
    )

    class Meta:
        model = City
        fields = ['id', 'name', 'province']


class SubdistrictFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    city = django_filters.CharFilter(name='city__name', lookup_type='iexact')

    class Meta:
        model = Subdistrict
        fields = ['id', 'name', 'city']


class VillageFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    name = django_filters.CharFilter(name='name', lookup_type='iexact')
    subdistrict = django_filters.CharFilter(
        name='subdistrict__name',
        lookup_type='iexact'
    )

    class Meta:
        model = Village
        fields = ['id', 'name', 'subdistrict']


class RWFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    village = django_filters.CharFilter(
        name='village__name',
        lookup_type='iexact'
    )

    class Meta:
        model = RW
        fields = ['id', 'village']


class RTFilter(filters.FilterSet):
    id = django_filters.NumberFilter(name='id')
    rw = django_filters.NumberFilter(name='rw__id')

    class Meta:
        model = RT
        fields = ['id', 'rw']
