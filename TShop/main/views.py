from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def index(request):
    return render(request, 'main/main.html')


def categories(request):
    all_categories = Categories.objects.all()
    context = {
        'cat_list': all_categories
    }
    return render(request, 'main/categories.html', context=context)


def product_view(request, url_slug):
    product_obj = get_object_or_404(Products, slug=url_slug)
    context = {
        'product_obj': product_obj
    }
    return render(request, 'main/product_temp.html', context=context)

