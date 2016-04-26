from django import template

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
