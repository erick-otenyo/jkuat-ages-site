from django.conf.urls import include, url

from activities import views

urlpatterns = [
	url(r'^', include([
		url(r'^$', views.activities_list, name='activity-list'),
		url(r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
	])),
 ]
