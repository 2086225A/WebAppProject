from django import template
from kinkyCuts.models import Creation

register = template.Library()

@register.inclusion_tag('kinkyCuts/creations.html')
def get_creation_list():
    return{'creations': Creation.objects.order_by('-likes')[:3]}
