from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView

from alumni.models import Alumni


class AlumniView(TemplateView): template_name = 'alumni.html'


# convert alumni model to Geojson for easier mapping
def alumni_geojs(request):
	alumni_as_geojson = serialize('geojson', Alumni.objects.all())
	return HttpResponse(alumni_as_geojson, content_type='application/json')
