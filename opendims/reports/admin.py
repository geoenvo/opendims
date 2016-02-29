#Core Django
from django.contrib import admin
from django.contrib.gis import admin

#Reports APP
from .models import Disaster, Source
from .models import Event
from .models import Report

##For import export CSV
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin


myModels = [Disaster,Source]


for myModel in myModels:
	def make_unverified(modeladmin, request,queryset):
		queryset.update(status = 'UN')


	make_unverified.short_description = ("Mark Event as Unverified")


	def make_verified(modeladmin, request, queryset):
		queryset.update(status = 'Ver')

	make_verified.short_description = "Mark Even as Verified"


        class ReportAdmin(admin.ModelAdmin):
                list_display = ['event', "source",'created', 'note', 'status']
		ordering = ['-created']
		actions = [make_verified, make_unverified]


	class EventAdmin(ImportExportModelAdmin, ExportActionModelAdmin, admin.ModelAdmin):
                actions = [make_verified, make_unverified]


	
admin.site.register(myModels,admin.OSMGeoAdmin)
admin.site.register(Report,ReportAdmin)
admin.site.register(Event,EventAdmin)




