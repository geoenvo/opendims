from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.conf import settings
import threading


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


try:
    from threading import local, current_thread
except ImportError:
    from django.utils._threading_local import local
 
_thread_locals = local()
 
 
class GlobalUserMiddleware(object):  # check http://kishorkumarmahato.com.np/django-get-current-user-globally-in-the-project/
    """
    Sets the current authenticated user in threading locals
 
    Usage example:
        from app_name.middleware import get_current_user
        user = get_current_user()
    """
    def process_request(self, request):
        setattr(
            _thread_locals,
            'user_{0}'.format(current_thread().name),
            request.user)
 
    def process_response(self, request, response):
 
        key = 'user_{0}'.format(current_thread().name)
 
        if not hasattr(_thread_locals, key):
            return response
 
        delattr(_thread_locals, key)
 
        return response
 
 
def get_current_user():
    return getattr(
        _thread_locals,
        'user_{0}'.format(current_thread().name),
        None)
