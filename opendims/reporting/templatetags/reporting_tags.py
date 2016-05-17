from reports.models import EventImpact

from django.template import Library
register = Library()


@register.filter
def running_total(eventimpacts):
    eventimpacts = EventImpact.objects.all()
    for eventimpact in eventimpacts:
        if eventimpact.evac_total:
            return sum([d.evac_total for d in eventimpacts])
        if eventimpact.affected_death:
            return sum([d.affected_death for d in eventimpacts])
        if eventimpact.affected_total:
            return sum([d.affected_total for d in eventimpacts])
