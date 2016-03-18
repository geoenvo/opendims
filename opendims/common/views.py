from django.contrib.auth.views import login as contrib_login
from django.shortcuts import redirect
from django.conf import settings

from rest_framework import generics, response, status


class CustomListCreateAPIView(generics.ListCreateAPIView):
    """
    Subclass API View to deal with django-filter strict not working. Overrides
    get method to check for invalid query params. If found return error 400.
    http://stackoverflow.com/questions/27182527
    """
    def is_valid_query_params(self, query_params):
        if query_params:
            valid_params = self.filter_class.Meta.fields
            # Accept default "format" parameter
            valid_params.append('format')
            query_params = [query_param.lower()
                            for query_param in query_params.keys()]
            invalid_params = set(query_params) - set(valid_params)
            if invalid_params:
                return False
        return True

    def get(self, request, *args, **kwargs):
        if not self.is_valid_query_params(request.query_params):
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        return super(CustomListCreateAPIView, self).get(
                                                    request, *args, **kwargs)


def login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return contrib_login(request, **kwargs)
