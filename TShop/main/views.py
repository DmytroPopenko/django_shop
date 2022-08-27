from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    all_products = Products.objects.all()
    context = {
        'prod_list': all_products
    }
    return render(request, 'main/main.html', context=context)


def categories(request):
    all_categories = Categories.objects.all()
    context = {
        'cat_list': all_categories
    }
    return render(request, 'main/categories.html', context=context)


def product_view(request, url_slug):
    product_obj = Products.objects.get(slug=url_slug)
    context = {
        'product_obj': product_obj
    }
    return render(request, 'main/product_temp.html', context=context)