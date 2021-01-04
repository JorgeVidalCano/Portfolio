from django import template
from mainApp.models import MetaData

register = template.Library()

@register.simple_tag
def metaDescription():
    return MetaData.objects.first().metaDescription