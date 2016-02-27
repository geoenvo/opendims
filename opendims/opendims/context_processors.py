from django.conf import settings

def resource_urls(request):
    resources_urls = dict(
        SITE_NAME = settings.SITE_NAME,
    )
    
    return resources_urls 
