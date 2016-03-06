from django.contrib.auth.views import login as contrib_login
from django.shortcuts import redirect
from django.conf import settings


def login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return contrib_login(request, **kwargs)
