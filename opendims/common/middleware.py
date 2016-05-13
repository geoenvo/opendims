from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.conf import settings


class AdminOnly404Middleware(object):
    """If in debug mode show default 404 error page only to admin users.
    """
    def process_response(self, request, response):
        if settings.DEBUG and isinstance(response, HttpResponseNotFound):
            if not request.user.is_superuser:
                return HttpResponseNotFound('<h1>Page not found</h1>')
        return response


class AdminOnly500Middleware(object):
    """If in debug mode show default 500 error page only to admin users.
    """
    def process_response(self, request, response):
        if settings.DEBUG and isinstance(response, HttpResponseServerError):
            if not request.user.is_superuser:
                return HttpResponseNotFound('<h1>Server error</h1>')
        return response


class AdminOnly403Middleware(object):
    """If in debug mode show default 403 error page only to admin users.
    """
    def process_response(self, request, response):
        if settings.DEBUG and isinstance(response, HttpResponseForbidden):
            if not request.user.is_superuser:
                return HttpResponseNotFound('<h1>Forbidden</h1>')
        return response
