from django.conf.urls import url
from companies import views

urlpatterns = [
	url(r'^$', views.CompanyView.as_view(), name='company-home'),
	url(r'^data/',views.companies_geojs, name='companies-data'),
]
