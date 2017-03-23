from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView

from companies.models import Company


class CompanyView(TemplateView): template_name = 'company.html'


# convert company model to Geojson for easier mapping
def companies_geojs(request):
	alumni_as_geojson = serialize('geojson', Company.objects.all())
	return HttpResponse(alumni_as_geojson, content_type='application/json')
