"""opendims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='opendims/opendims_page_home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='opendims/opendims_page_about.html'), name='page_about'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': reverse_lazy('home')}, name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^reports/', include('reports.urls', namespace='reports')),

]

admin.site.site_header = ''.join((settings.SITE_NAME, ' administration'))
admin.site.site_title = ''.join((settings.SITE_NAME, ' site admin'))
