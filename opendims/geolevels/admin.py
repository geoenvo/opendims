from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin


from geolevels.models import Province, City, Subdistrict, Village, RW, RT

myModels=[Province, City, Subdistrict, Village, RW, RT]


admin.site.register(myModels,OSMGeoAdmin)

# Register your models here.
