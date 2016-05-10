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
