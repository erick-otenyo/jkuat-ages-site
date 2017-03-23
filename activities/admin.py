from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from activities.models import Activity


class ActivityAdmin(LeafletGeoAdmin):
	list_display = ['name', 'date', 'slug']
	prepopulated_fields = {'slug': ('date',)}


admin.site.register(Activity, ActivityAdmin)
