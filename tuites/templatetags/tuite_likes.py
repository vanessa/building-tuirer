from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag(takes_context=True)
def tuite_liked_icon(context):
    user = context.get('user')
    tuite = context.get('tuite')
    user_has_liked = tuite.liked_by.filter(pk=user.pk).exists()

    if user_has_liked:
        return format_html('<i class="fas fa-heart"></i>')
    return format_html('<i class="far fa-heart"></i>')
