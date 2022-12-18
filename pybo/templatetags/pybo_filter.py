from django import template

register = template.Library()


@register.filter
def sub(value: int, arg: int) -> int:
    return value - arg
