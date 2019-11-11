from django.conf.urls import include,url
from views import HomepageView, county_dataset,incidences_dataset

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^county_data/', county_dataset, name='county'),
    url(r'^incidence_data/', incidences_dataset, name='incidences'),


]
