from django import template

register = template.Library()


@register.simple_tag
def subtract(value, arg):
    return value - arg
