from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from dal import autocomplete
from rest_framework import generics, filters

from common.views import CustomListAPIView
from .models import Province, City, Subdistrict, Village, RW, RT
from .serializers import ProvinceSerializer, CitySerializer, SubdistrictSerializer, VillageSerializer, RWSerializer, RTSerializer
from .filters import ProvinceFilter, CityFilter, SubdistrictFilter, VillageFilter, RWFilter, RTFilter


class APIProvinceList(CustomListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = ProvinceFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APICityList(CustomListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = CityFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APISubdistrictList(CustomListAPIView):
    queryset = Subdistrict.objects.all()
    serializer_class = SubdistrictSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = SubdistrictFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APIVillageList(CustomListAPIView):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = VillageFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APIRWList(CustomListAPIView):
    queryset = RW.objects.all()
    serializer_class = RWSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = RWFilter
    ordering_fields = ('id',)
    ordering = ('-id',)


class APIRTList(CustomListAPIView):
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


class ProvinceListView(generic.ListView):
    queryset = Province.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE


class ProvinceDetailView(generic.DetailView):
    model = Province

    def get_context_data(self, **kwargs):
        context = super(ProvinceDetailView, self).get_context_data(**kwargs)
        context['cities'] = City.objects.filter(province=self.get_object()).order_by('name')
        return context


class CityListView(generic.ListView):
    queryset = City.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE


class CityDetailView(generic.DetailView):
    model = City

    def get_context_data(self, **kwargs):
        context = super(CityDetailView, self).get_context_data(**kwargs)
        context['subdistricts'] = Subdistrict.objects.filter(city=self.get_object()).order_by('name')
        return context


class SubdistrictListView(generic.ListView):
    queryset = Subdistrict.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE


class SubdistrictDetailView(generic.DetailView):
    model = Subdistrict

    def get_context_data(self, **kwargs):
        context = super(SubdistrictDetailView, self).get_context_data(**kwargs)
        context['villages'] = Village.objects.filter(subdistrict=self.get_object()).order_by('name')
        return context


class VillageListView(generic.ListView):
    queryset = Village.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE


class VillageDetailView(generic.DetailView):
    model = Village

    def get_context_data(self, **kwargs):
        context = super(VillageDetailView, self).get_context_data(**kwargs)
        context['rws'] = RW.objects.filter(village=self.get_object()).order_by('name')
        return context


class RWListView(generic.ListView):
    queryset = RW.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE


class RWDetailView(generic.DetailView):
    model = RW

    def get_context_data(self, **kwargs):
        context = super(RWDetailView, self).get_context_data(**kwargs)
        context['rts'] = RT.objects.filter(rw=self.get_object()).order_by('name')
        return context


class RTListView(generic.ListView):
    queryset = RT.objects.order_by('name')
    paginate_by = settings.ITEMS_PER_PAGE


class RTDetailView(generic.DetailView):
    model = RT

    def get_context_data(self, **kwargs):
        context = super(RTDetailView, self).get_context_data(**kwargs)
        return context
