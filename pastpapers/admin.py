from django.contrib import admin
from .models import Paper
# Register your models here.
class PaperAdmin(admin.ModelAdmin):
	list_display = ['unit_title','year','course','date','slug']
	prepopulated_fields = {'slug': ('date',)}

admin.site.register(Paper,PaperAdmin)

