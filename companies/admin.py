from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from companies.models import Company

admin.site.register(Company, LeafletGeoAdmin)
