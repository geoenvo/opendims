from django.contrib.gis import admin

from .models import Province, City, Subdistrict, Village, RW, RT


class ProvinceAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'name', 'note')


class CityAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'province', 'name', 'note')


class SubdistrictAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'city', 'name', 'note')


class VillageAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'subdistrict', 'name', 'note')


class RWAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'village', 'name', 'note')


class RTAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'rw', 'name', 'note')


admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Subdistrict, SubdistrictAdmin)
admin.site.register(Village, VillageAdmin)
admin.site.register(RW, RWAdmin)
admin.site.register(RT, RTAdmin)
