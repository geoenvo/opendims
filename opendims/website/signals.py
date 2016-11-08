from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import Signal
from django.dispatch import receiver

from actstream import action
from actstream.models import Action

from common.middleware import get_current_user
from website.models import Actor, Verb, Object, Post, SiteHeader, Welcome, Partner, Link, Resource, Video
from waterlevel.models import WaterLevelReport, WaterGate
from reporting.models import Report, Template
from reports.models import Event
from earlywarning.models import EarlyWarningReport
from automaticweathersystem.models import SensorReport
from weatherforecast.models import WeatherForecastReport
from disasterrehabilitation.models import EventAssessment
from reportaggregator.models import Source, Keyword


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
def waterlevel_report_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing WaterLevelReport
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='waterlevel_report_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.watergate)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='sensor_report_adding')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def watergate_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing WaterGate
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='watergate_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='wategate_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def event_reporting_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Event
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='event_report_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.disaster)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='event_report_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.disaster)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def early_warning_report_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing EarlyWarningReport
    """
    user = get_current_user()
    
    if kwargs.get('created', False):    
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='early_warning_report_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='early_warning_report_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def sensor_report_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing SensorReport
    """
    user = get_current_user()
    
    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='sensor_report_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='sensor_report_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.sensorstation)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def weather_forcast_report_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing WeatherForecastReport
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='weather_forecast_report_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.city)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='weather_forecast_report_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.city)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def pusdalops_report_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Pusdalops Report
    """
    user = instance.author

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='pusdalops_report_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.type)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='pusdalops_report_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.type)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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


@receiver(post_save, sender=Template)
def pusdalops_template_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Pusdalops Template
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='pusdalops_template_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='pusdalops_template_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


@receiver(post_delete, sender=Template)
def pusdalops_template_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Pusdalops Template
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='pusdalops_template_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Post)
def website_post_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Post Website
    """
    user = instance.author
 
    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='website_post_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='website_post_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def website_siteheader_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing SiteHeader Website
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='website_siteheader_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='website_siteheader_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def website_welcome_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Welcome Website
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='website_welcome_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='website_welcome_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def website_partner_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Partner Website
    """
    user = get_current_user()

    if kwargs.get('created', False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='website_partner_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='website_partner_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def website_resource_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Resource Website
    """
    user = get_current_user()

    if kwargs.get("created", False):
        add_actor = Actor.objects.get(user=user)
        add_activity = Verb.objects.get(name='website_resource_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='website_resource_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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
def website_video_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Video Website
    """
    user = get_current_user()
 
    if kwargs.get("created", False):
        add_actor = Actor.objects.get(user=user)    
        add_activity = Verb.objects.get(name='website_video_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='website_video_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.title)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


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


@receiver(post_save, sender=EventAssessment)
def event_assessment_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Event Assessment Disaster Rehabilitation
    """
    user = get_current_user()
 
    if kwargs.get("created", False):
        add_actor = Actor.objects.get(user=user)    
        add_activity = Verb.objects.get(name='event_assessment_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='event_assessment_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


@receiver(post_delete, sender=EventAssessment)
def event_assessment_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Event Assessment Disaster Rehabilitation
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='event_assessment_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Source)
def report_aggregator_source_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Source in Report Aggregator
    """
    user = get_current_user()
 
    if kwargs.get("created", False):
        add_actor = Actor.objects.get(user=user)    
        add_activity = Verb.objects.get(name='report_aggregator_source_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='report_aggregator_source_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


@receiver(post_delete, sender=Source)
def report_aggregator_source_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Source in Report Aggregator
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='report_aggregator_source_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)


@receiver(post_save, sender=Keyword)
def report_aggregator_keyword_add_or_edit(sender, instance, **kwargs):
    """
    receive signals when user adding/editing Keyword in Report Aggregator
    """
    user = get_current_user()
 
    if kwargs.get("created", False):
        add_actor = Actor.objects.get(user=user)    
        add_activity = Verb.objects.get(name='report_aggregator_keyword_adding')
        add_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.keyword)
        action.send(add_actor, verb=add_activity, description=add_activity.description, action_object=add_object)
    else:
        edit_actor = Actor.objects.get(user=user)
        edit_activity = Verb.objects.get(name='report_aggregator_keyword_editing')
        edit_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.name)
        action.send(edit_actor, verb=edit_activity, description=edit_activity.description, action_object=edit_object)


@receiver(post_delete, sender=Keyword)
def report_aggregator_keyword_delete(sender, instance, **kwargs):
    """
    receive signals when user deleting Keyword in Report Aggregator
    """
    user = get_current_user()
    delete_actor = Actor.objects.get(user=user)
    delete_activity = Verb.objects.get(name='report_aggregator_keyword_deleting')
    delete_object = Object.objects.create(obj_id=instance.pk, obj_text=instance.keyword)
    action.send(delete_actor, verb=delete_activity, description=delete_activity.description, action_object=delete_object)
