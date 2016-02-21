
#django

from django.contrib import admin
from django.contrib.gis import admin
from .models import Disaster, Event, Source
from .models import Report

myModels=[Event,Disaster,Source]

for myModel in myModels:
	def make_verified(modeladmin, request, queryset):
		queryset.update(status='Ver')

	make_verified.short_description="Mark Event as Verified"

	class ReportAdmin(admin.ModelAdmin):
		list_display=["event", "source",'created', 'note', 'status']
		ordering=['event']
		actions=[make_verified]
	
admin.site.register(myModels,admin.OSMGeoAdmin)
admin.site.register(Report,ReportAdmin)
