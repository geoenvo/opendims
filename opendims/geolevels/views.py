from django.shortcuts import render, get_object_or_404
from .models import Province, City, Subdistrict, Village, RT, RW


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
    rt = get_object_or_404(Province, pk=pk)
    context = {'rt': rt}
    return render(request, 'geolevels/rt_detail.html', context)

