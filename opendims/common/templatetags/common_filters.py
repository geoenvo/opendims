import os

from django import template

register = template.Library()


@register.filter
def loop(number):
    return range(number)


@register.filter
def filename(value):
    return os.path.basename(value.file.name)
