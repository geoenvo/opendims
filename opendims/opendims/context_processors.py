from django.conf import settings


def resource_urls(request):
    resources_urls = dict(
        SITE_NAME=settings.SITE_NAME,
        DEFAULT_CENTER=settings.LEAFLET_CONFIG['DEFAULT_CENTER'],
        DEFAULT_ZOOM=settings.LEAFLET_CONFIG['DEFAULT_ZOOM'],
    )

    return resources_urls
