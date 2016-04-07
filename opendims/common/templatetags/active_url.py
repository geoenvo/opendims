from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def active_url(request, url_name, by_path=False):
    """ Return the string 'active' if current request.path is same as name

    Args:
        request: Django request object
        url_name: name of the url or the actual path
        by_path: True if name contains a url instead of url name
    """
    if by_path:
        path = url_name
    else:
        path = reverse(url_name)

    if request.path == path:
        return 'active'

    return ''
