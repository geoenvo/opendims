from django.conf import settings


def resource_urls(request):
    resources_urls = dict(
        SITE_NAME=settings.SITE_NAME,
        DEFAULT_CENTER=settings.LEAFLET_CONFIG['DEFAULT_CENTER'],
        DEFAULT_ZOOM=settings.LEAFLET_CONFIG['DEFAULT_ZOOM'],
        DEFAULT_CENTER_WATERLEVEL=settings.DEFAULT_CENTER_WATERLEVEL,
        DEFAULT_ZOOM_WATERLEVEL=settings.DEFAULT_ZOOM_WATERLEVEL,
        DISASTER_STATISTICS=settings.DISASTER_STATISTICS,
        WEATHERFORECAST_CITIES=settings.WEATHERFORECAST_CITIES
    )

    return resources_urls
