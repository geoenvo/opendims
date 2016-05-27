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


class ForceDefaultLanguageMiddleware(object):
    """
    Ignore Accept-Language HTTP headers

    This will force the I18N machinery to always choose settings.LANGUAGE_CODE
    as the default initial language, unless another one is set via sessions or cookies.

    Should be installed *before* any middleware that checks request.META['HTTP_ACCEPT_LANGUAGE'],
    namely django.middleware.locale.LocaleMiddleware.
    """
    def process_request(self, request):
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']
