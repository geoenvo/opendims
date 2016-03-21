from django.shortcuts import render, get_object_or_404

from dal import autocomplete

from .models import Province, City, Subdistrict, Village, RW, RT
from reports.views import CustomListCreateAPIView

from django.views import generic
from django.conf import settings

from .serializers import ProvinceSerializer, CitySerializer, SubdistrictSerializer, VillageSerializer, RWSerializer, RTSerializer
from rest_framework import generics, filters, response, status

from .filters import ProvinceFilter, CityFilter, SubdistrictFilter, VillageFilter, RWFilter, RTFilter


class APIProvinceList(CustomListCreateAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = ProvinceFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APICityList(CustomListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = CityFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APISubdistrictList(CustomListCreateAPIView):
    queryset = Subdistrict.objects.all()
    serializer_class = SubdistrictSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = SubdistrictFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APIVillageList(CustomListCreateAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = VillageFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APIRWList(CustomListCreateAPIView):
    queryset = RW.objects.all()
    serializer_class = RWSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = RWFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APIRTList(CustomListCreateAPIView):
    queryset = RT.objects.all()
    serializer_class = RTSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = RTFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class AutocompleteProvince(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Province.objects.none()
        queryset = Province.objects.all().order_by('name')
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


class AutocompleteCity(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return City.objects.none()
        queryset = City.objects.all().order_by('name')
        province = self.forwarded.get('province', None)
        if province:
            queryset = queryset.filter(province=province)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


class AutocompleteSubdistrict(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Subdistrict.objects.none()
        queryset = Subdistrict.objects.all().order_by('name')
        city = self.forwarded.get('city', None)
        if city:
            queryset = queryset.filter(city=city)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


class AutocompleteVillage(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Village.objects.none()
        queryset = Village.objects.all().order_by('name')
        subdistrict = self.forwarded.get('subdistrict', None)
        if subdistrict:
            queryset = queryset.filter(subdistrict=subdistrict)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


class AutocompleteRW(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return RW.objects.none()
        queryset = RW.objects.all().order_by('name')
        village = self.forwarded.get('village', None)
        if village:
            queryset = queryset.filter(village=village)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


class AutocompleteRT(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return RT.objects.none()
        queryset = RT.objects.all().order_by('name')
        rw = self.forwarded.get('rw', None)
        if rw:
            queryset = queryset.filter(rw=rw)
        if self.q:
            queryset = queryset.filter(name__icontains=self.q)
        return queryset


def province_list(request):
    provinces = Province.objects.all().order_by('name')
    context = {'provinces': provinces}
    return render(request, 'geolevels/province_list.html', context)


def province_detail(request, pk):
    province = get_object_or_404(Province, pk=pk)
    cities = City.objects.all().order_by('name')
    context = {'province': province, 'cities': cities}
    return render(request, 'geolevels/province_detail.html', context)


def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    subdistricts = Subdistrict.objects.all().order_by('name')
    context = {'city': city, 'subdistricts': subdistricts}
    return render(request, 'geolevels/city_detail.html', context)


def subdistrict_detail(request, pk):
    subdistrict = get_object_or_404(Subdistrict, pk=pk)
    villages = Village.objects.all().order_by('name')
    context = {'subdistrict': subdistrict, 'villages': villages}
    return render(request, 'geolevels/subdistrict_detail.html', context)


def village_detail(request, pk):
    village = get_object_or_404(Village, pk=pk)
    rws = RW.objects.all().order_by('name')
    context = {'village': village, 'rws': rws}
    return render(request, 'geolevels/village_detail.html', context)


def rw_detail(request, pk):
    rw = get_object_or_404(RW, pk=pk)
    rts = RT.objects.all().order_by('name')
    context = {'rw': rw, 'rts': rts}
    return render(request, 'geolevels/rw_detail.html', context)


def rt_detail(request, pk):
    rt = get_object_or_404(RT, pk=pk)
    context = {'rt': rt}
    return render(request, 'geolevels/rt_detail.html', context)
