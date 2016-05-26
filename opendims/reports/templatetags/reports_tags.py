from django import template
from django.template import Library
from django.utils import timezone

from reports.models import Event
from django.db.models import Sum


register = Library()
register = template.Library()


@register.filter
def eventimpacts_total(eventimpacts):
    return sum([d.evac_total for d in eventimpacts])


def total_event(events):
    return sum([event.height for event in events])


@register.simple_tag
def get_event_statistics(disaster, month, year):
    month = timezone.localtime(timezone.now()).month
    year = timezone.localtime(timezone.now()).year
    events_with_impacts = Event.objects.filter(
        eventimpacts__isnull=False, disaster=disaster,
        created__month=month, created__year=year
    ).distinct()
    events_with_impacts = events_with_impacts.annotate(
        evac_total=Sum('eventimpacts__evac_total'),
        affected_total=Sum('eventimpacts__affected_total'),
        affected_injury=Sum('eventimpacts__affected_injury'),
        affected_death=Sum('eventimpacts__affected_death'),
        loss_total=Sum('eventimpacts__loss_total')
    )
    return events_with_impacts


@register.simple_tag
def get_eventimpact_total(event_statistics):
    eventimpact_total = {
        'evac_total': 0,
        'affected_total': 0,
        'affected_injury': 0,
        'affected_death': 0,
        'loss_total': 0
    }
    for event_statistic in event_statistics:
        if event_statistic.evac_total:
            eventimpact_total['evac_total'] += event_statistic.evac_total
        if event_statistic.affected_total:
            eventimpact_total['affected_total'] += event_statistic.affected_total
        if event_statistic.affected_injury:
            eventimpact_total['affected_injury'] += event_statistic.affected_injury
        if event_statistic.affected_death:
            eventimpact_total['affected_death'] += event_statistic.affected_death
        if event_statistic.loss_total:
            eventimpact_total['loss_total'] += event_statistic.loss_total
    return eventimpact_total
