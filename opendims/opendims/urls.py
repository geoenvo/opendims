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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.flatpages import urls as flatpages_urls

from registration.backends.default import urls as registration_urls
from ckeditor_uploader import urls as ckeditor_uploader_urls

from common import views as common_views
from reports import urls as reports_urls
from geolevels import urls as geolevels_urls
from maps import urls as maps_urls
from jaksafe import urls as jaksafe_urls
from waterlevel import urls as waterlevel_urls

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='opendims/page_home.html'), name='home'),
    url(r'^bootleaf_example/$', TemplateView.as_view(template_name='bootleaf_example/example.html'), name='bootleaf_example'),
    url(r'^bootleaf_test/$', TemplateView.as_view(template_name='bootleaf_example/test.html'), name='bootleaf_test'),
    url(r'^accounts/login/$', common_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': reverse_lazy('home')}, name='logout'),
    url(r'^accounts/', include(registration_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include(flatpages_urls)),
    url(r'^ckeditor/', include(ckeditor_uploader_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^reports/', include(reports_urls, namespace='reports')),
    url(r'^geolevels/', include(geolevels_urls, namespace='geolevels')),
    url(r'^maps/', include(maps_urls, namespace='maps')),
    url(r'^jaksafe/', include(jaksafe_urls, namespace='jaksafe')),
    url(r'^waterlevel/', include(waterlevel_urls, namespace='waterlevel')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

admin.site.site_header = ''.join((settings.SITE_NAME, ' administration'))
admin.site.site_title = ''.join((settings.SITE_NAME, ' site admin'))
