from django.contrib import admin
from django.contrib.gis import admin
from .models import Disaster, Event, Source
from .models import Report
# Register your models here.

myModels=[Event,Disaster,Source]




class ReportAdmin(admin.ModelAdmin):
	list_display=["event", 'source', 'status']
	ordering=['event']
	


admin.site.register(myModels,admin.OSMGeoAdmin)
admin.site.register(Report,ReportAdmin)
