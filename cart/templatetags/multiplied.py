from django import template

register = template.Library()
@register.simple_tag
def multiplied(price, count):
    return price*count