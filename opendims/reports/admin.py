from django.contrib import admin
from django.contrib.gis import admin
from .models import Disaster, Event, Source
from .models import Report


myModels=[Event,Disaster,Source]

for myModel in myModels:
	def make_updated(modeladmin, request, queryset):
		queryset.update(status='u')

	make_updated.short_description="Mark Event as updated"



	class ReportAdmin(admin.ModelAdmin):
		list_display=["event", 'source', 'status', 'note']
		ordering=['event']
		actions=[make_updated]
	
admin.site.register(myModels,admin.OSMGeoAdmin)
admin.site.register(Report,ReportAdmin)
