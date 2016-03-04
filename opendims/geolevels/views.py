from django.shortcuts import render, get_object_or_404
from .models import Province, City, Subdistrict, Village, RT, RW


def province_list(request):
	provinces = Province.objects.all().order_by('name')
	context = {'provinces': provinces}
	return render(request, 'geolevels/province_list.html', context)

def province_detail(request, pk):
    province = get_object_or_404(Province, pk=pk)
    context = {'province': province}
    return render(request, 'geolevels/province_detail.html', context)

def city_detail(request, pk):
    city= get_object_or_404(City, pk=pk).order_by('name')
    context = {'city': city}
    return render(request, 'geolevels/city_detail.html', context)

def subdistrict_detail(request, pk):
    subdistrict = get_object_or_404(Subdistrict, pk=pk)
    context = {'subdistrict': subdistrict}
    return render(request, 'geolevels/subdistrict_detail.html', context)

def village_detail(request, pk):
    village = get_object_or_404(Village, pk=pk)
    context = {'village': village}
    return render(request, 'geolevels/village_detail.html', context)

def rw_detail(request, pk):
    rw= get_object_or_404(RW, pk=pk)
    context = {'rw': rw}
    return render(request, 'geolevels/rw_detail.html', context)

def rt_detail(request, pk):
    rt = get_object_or_404(Province, pk=pk)
    context = {'rt': rt}
    return render(request, 'geolevels/rt_detail.html', context)

