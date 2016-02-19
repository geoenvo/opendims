from django.contrib import admin
from django.contrib.gis import admin
from .models import Disaster, Event, Source, Report
# Register your models here.

myModels=[Event,Disaster,Source,Report]

admin.site.register(myModels, admin.OSMGeoAdmin)
