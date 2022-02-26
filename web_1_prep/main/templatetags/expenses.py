from django import template

from web_1_prep.main.models import Expense

register = template.Library()


@register.simple_tag()
def expenses_exist():
    return Expense.objects.count() > 0