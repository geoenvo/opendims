import datetime

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def subtract(value, arg):
    return value - arg


@register.simple_tag
def query(qs, **kwargs):
    """Template tag for queryset filtering.

    Usage:
        {% query objects field=value as myobjects %}
        {% for object in myobjects %}
        ...
        {% endfor %}
    """
    return qs.filter(**kwargs)


@register.simple_tag
def to_list(*args):
    """Template tag for creating a list.

    Usage:
        {% to_list 'a' 1 2 3 as my_list %}
        {% for list_item in my_list %}
        ...
        {% endfor %}
    """
    return args


@register.simple_tag
def settings_value(name):
    """Get a value from the settings file.

    Usage:
        {% settings_value "SETTINGS_NAME" %}
    """
    return getattr(settings, name, '')


@register.simple_tag
def copyright_years(start_year):
    """
    """
    current_year = datetime.datetime.now().year
    if start_year < current_year:
        return "{} - {}".format(str(start_year), str(current_year))
    else:
        return start_year
