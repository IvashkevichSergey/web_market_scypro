from pathlib import Path
from os import path

from django import template

register = template.Library()


@register.filter()
def mediapath(path_to_image):
    return f'/media/{path_to_image}'


@register.simple_tag()
def mediapath(path_to_image):
    return f'/media/{path_to_image}'