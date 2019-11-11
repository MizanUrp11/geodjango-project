from django.contrib import admin
from .models import ReporterModel,Counties
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class ReporterModelFields(LeafletGeoAdmin):
    list_display = ('name','location')

class CountiesFields(LeafletGeoAdmin):
    list_display = ('counties','codes','cty_code')

admin.site.register(ReporterModel,ReporterModelFields)
admin.site.register(Counties,CountiesFields)