from django.conf.urls import url
from alumni import views

urlpatterns = [
	url(r'^$', views.AlumniView.as_view(), name='alumi-home'),
	url(r'^data/',views.alumni_geojs, name='alumi-data'),
]
