from django import template

from web_1_prep.main.models import Profile

register = template.Library()


@register.simple_tag()
def profiles_exist():
    return Profile.objects.count() > 0