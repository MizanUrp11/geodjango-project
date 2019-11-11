from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties,ReporterModel
# Create your views here.

class HomepageView(TemplateView):
    template_name = 'index.html' 

def county_dataset(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties,content_type='json')

def incidences_dataset(request):
    incidences = serialize('geojson', ReporterModel.objects.all())
    return HttpResponse(incidences,content_type='json')