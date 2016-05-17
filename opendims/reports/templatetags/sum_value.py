from django.template import Library
register = Library()


@register.filter
def eventimpacts_total(eventimpacts):
    return sum([d.evac_total for d in eventimpacts])


def total_event(events):
    return sum([event.height for event in events])
