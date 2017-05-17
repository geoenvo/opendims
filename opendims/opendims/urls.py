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
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.flatpages import urls as flatpages_urls

from registration.backends.default import urls as registration_urls
from ckeditor_uploader import urls as ckeditor_uploader_urls
from django_rq import urls as django_rq_urls

from common import views as common_views
from reports import urls as reports_urls
from geolevels import urls as geolevels_urls
from maps import urls as maps_urls
from jaksafe import urls as jaksafe_urls
from waterlevel import urls as waterlevel_urls
from contact import urls as contact_urls
from weatherforecast import urls as weatherforecast_urls
from disasterrehabilitation import urls as disasterrehabilitation_urls
from reporting import urls as reporting_urls
from website import urls as website_urls
from earlywarning import urls as earlywarning_urls
from automaticweathersystem import urls as aws_urls


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

adminurlpattern = [url(r'^admin/', admin.site.urls)]

if settings.PRODUCTION:
    adminurlpattern = [url(settings.ADMINURLPATTERN, admin.site.urls)] # Use secret admin URL in production mode

urlpatterns = adminurlpattern + [
    url(r'^$', TemplateView.as_view(template_name='opendims/page_home.html'), name='home'),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/login/$', common_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': reverse_lazy('home')}, name='logout'),
    url(r'^accounts/', include(registration_urls)),
    url(r'^pages/', include(flatpages_urls)),
    url(r'^ckeditor/', include(ckeditor_uploader_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^capture/', include('screamshot.urls', namespace='screamshot')),
    url(r'^django-rq/', include(django_rq_urls)),
    url(r'^reports/', include(reports_urls, namespace='reports')),
    url(r'^geolevels/', include(geolevels_urls, namespace='geolevels')),
    url(r'^maps/', include(maps_urls, namespace='maps')),
    url(r'^jaksafe/', include(jaksafe_urls, namespace='jaksafe')),
    url(r'^waterlevel/', include(waterlevel_urls, namespace='waterlevel')),
    url(r'^contact/', include(contact_urls, namespace='contact')),
    url(r'^weatherforecast/', include(weatherforecast_urls, namespace='weatherforecast')),
    url(r'^rehabilitation/', include(disasterrehabilitation_urls, namespace='disasterrehabilitation')),
    url(r'^reporting/', include(reporting_urls, namespace='reporting')),
    url(r'^web/', include(website_urls, namespace='website')),
    url(r'^earlywarning/', include(earlywarning_urls, namespace='earlywarning')),
    url(r'^aws/', include(aws_urls, namespace='aws'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

admin.site.site_header = ''.join((settings.SITE_NAME, ' administration'))
admin.site.site_title = ''.join((settings.SITE_NAME, ' site admin'))
