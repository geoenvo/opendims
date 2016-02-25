from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin


from geolevels.models import Province, City, Subdistrict, Village, RW

myModels=[Province, City, Subdistrict, Village, RW]


admin.site.register(myModels,OSMGeoAdmin)

# Register your models here.
