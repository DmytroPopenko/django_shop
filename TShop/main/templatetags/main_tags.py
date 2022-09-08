from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_products():
    return Products.objects.all()
@register.inclusion_tag('main/cat_list.html')
def get_categories_list():
    categories = Categories.objects.all()
    return {'categories': categories}