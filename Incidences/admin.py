from django.contrib import admin
from .models import ReporterModel
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class ReporterModelFields(LeafletGeoAdmin):
    pass
    # list_display = ('name','location')

admin.site.register(ReporterModel,ReporterModelFields)
