from django.shortcuts import render, get_object_or_404

from dal import autocomplete

from .models import Province, City, Subdistrict, Village, RW, RT


class AutocompleteProvince(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Province.objects.none()
        qs = Province.objects.all().order_by('name')
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class AutocompleteCity(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return City.objects.none()
        qs = City.objects.all().order_by('name')
        province = self.forwarded.get('province', None)
        if province:
            qs = qs.filter(province=province)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class AutocompleteSubdistrict(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Subdistrict.objects.none()
        qs = Subdistrict.objects.all().order_by('name')
        city = self.forwarded.get('city', None)
        if city:
            qs = qs.filter(city=city)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class AutocompleteVillage(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Village.objects.none()
        qs = Village.objects.all().order_by('name')
        subdistrict = self.forwarded.get('subdistrict', None)
        if subdistrict:
            qs = qs.filter(subdistrict=subdistrict)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class AutocompleteRW(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return RW.objects.none()
        qs = RW.objects.all().order_by('name')
        village = self.forwarded.get('village', None)
        if village:
            qs = qs.filter(village=village)
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


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
    city= get_object_or_404(City, pk=pk)
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
    rw= get_object_or_404(RW, pk=pk)
    rts = RT.objects.all().order_by('name')
    context = {'rw': rw, 'rts': rts}
    return render(request, 'geolevels/rw_detail.html', context)

def rt_detail(request, pk):
    rt = get_object_or_404(RT, pk=pk)
    context = {'rt': rt}
    return render(request, 'geolevels/rt_detail.html', context)

