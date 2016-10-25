from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch.dispatcher import Signal
from django.dispatch import receiver

from actstream import action
from actstream.models import Action

from website.models import Actor, Verb, Object


@receiver(user_logged_in)
def user_logged_in(user, **kwargs):
    """
    receive signals when user login
    """
    if not Actor.objects.filter(user=user).exists():
        Actor.objects.create(user=user)
    login_actor = Actor.objects.get(user=user)
    login_activity = Verb.objects.get(name='login')
    action.send(login_actor, verb=login_activity, description=login_activity.description)


@receiver(user_logged_out)
def user_logged_out(user, **kwargs):
    """
    receive signals when user logout
    """
    logout_actor = Actor.objects.get(user=user)
    logout_activity = Verb.objects.get(name='logout')
    action.send(logout_actor, verb=logout_activity, description=logout_activity.description)


def waterlevel_report_edited(user, **kwargs):
	"""
	when, whom, do waterlevel report edited
	"""