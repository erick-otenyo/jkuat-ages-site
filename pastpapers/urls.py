from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from pastpapers import views

# PastPapers URLS
urlpatterns = [
	url(r'^$', views.PastpaperView.as_view(), name='pastpapers'),
	url(r'^first-year/', include([
		url(r'^$', views.first_year, name='first_year_list'),
		url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.paper_detail, name='paper_detail_1'),
	])),
	url(r'^second-year/', include([
		url(r'^$', views.second_year, name='second_year_list'),
		url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.paper_detail, name='paper_detail_2'),
	])),
	url(r'^third-year/', include([
		url(r'^$', views.third_year, name='third_year_list'),
		url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.paper_detail, name='paper_detail_3'),
	])),
	url(r'^fourth-year/', include([
		url(r'^$', views.fourth_year, name='fourth_year_list'),
		url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.paper_detail, name='paper_detail_4'),
	])),
	url(r'^fifth-year/', include([
		url(r'^$', views.fifth_year, name='fifth_year_list'),
		url(r'^(?P<id>\d+)/(?P<slug>\d+)/$', views.paper_detail, name='paper_detail_5'),
	])),
]