from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import Signal
from django.dispatch import receiver

from actstream import action
from actstream.models import Action

from common.middleware import get_current_user
from website.models import Actor, Verb, Object, Post, SiteHeader, Welcome, Partner, Link, Resource, Video
from waterlevel.models import WaterLevelReport, WaterGate
from reporting.models import Report
from reports.models import Event
from earlywarning.models import EarlyWarningReport
from automaticweathersystem.models import SensorReport
from weatherforecast.models import WeatherForecastReport
from reporting.models import Report



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


@receiver(post_save, sender=WaterLevelReport)
def waterlevel_report_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing WaterLevelReport
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='waterlevel_report_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.watergate)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=WaterLevelReport)
def waterlevel_report_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting WaterLevelReport
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='waterlevel_report_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.watergate)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=WaterGate)
def watergate_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing WaterGate
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='watergate_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=WaterGate)
def watergate_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting WaterGate
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='watergate_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Event)
def event_reporting_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Event
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='event_report_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.disaster)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Event)
def event_reporting_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Event
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='event_report_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.disaster)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=EarlyWarningReport)
def early_warning_report_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing EarlyWarningReport
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='early_warning_report_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=EarlyWarningReport)
def early_warning_report_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting EarlyWarningReport
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='early_warning_report_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=SensorReport)
def sensor_report_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing SensorReport
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='sensor_report_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=SensorReport)
def sensor_report_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting SensorReport
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='sensor_report_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=WeatherForecastReport)
def weather_forcast_report_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing WeatherForecastReport
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='weather_forecast_report_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.city)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=WeatherForecastReport)
def weather_forcast_report_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting WeatherForecastReport
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='weather_forecast_report_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.city)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Report)
def pusdalops_report_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Pusdalops Report
    """
    user = instance.author
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='pusdalops_report_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.type)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Report)
def pusdalops_report_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Pusdalops Report
    """
    user = instance.author
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='pusdalops_report_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.type)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Post)
def website_post_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Post Website
    """
    user = instance.author
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='website_post_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Post)
def website_post_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Post Website
    """
    user = instance.author
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='website_post_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=SiteHeader)
def website_siteheader_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing SiteHeader Website
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='website_siteheader_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=SiteHeader)
def website_siteheader_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting SiteHeader Website
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='website_siteheader_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Welcome)
def website_welcome_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Welcome Website
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='website_welcome_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Welcome)
def website_welcome_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Welcome Website
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='website_welcome_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Partner)
def website_partner_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Partner Website
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='website_partner_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Partner)
def website_partner_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Partner Website
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='website_partner_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Resource)
def website_resource_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Resource Website
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='website_resource_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Partner)
def website_resource_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Resource Website
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='website_resource_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Video)
def website_video_added(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Video Website
    """
    user = get_current_user()
    add_actor = Actor.objects.get(user=user)
    add_activity = Verb.objects.get(name='website_video_adding')
    add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)


@receiver(post_delete, sender=Video)
def website_video_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Video Website
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='website_video_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)
    