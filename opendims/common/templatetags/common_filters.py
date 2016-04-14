from django import template

register = template.Library()


@register.filter
def loop(number):
    return range(number)
