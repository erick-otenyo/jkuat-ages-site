"""ages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from ages.views import HomeView, ControlsView, AlumniView

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^alumni/', AlumniView.as_view(), name='alumni'),
	url(r'^companies/', include('companies.urls')),
	url(r'^activities/', include('activities.urls')),
	url(r'^past-papers/', include('pastpapers.urls')),
	url(r'^controls/', ControlsView.as_view(), name='controls-view'),

]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)