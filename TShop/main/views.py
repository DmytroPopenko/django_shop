from django.shortcuts import render
from .models import Products


# Create your views here.
def index(request):
    all_products = Products.objects.all()
    context = {
        'prod_list': all_products
    }
    return render(request, 'main/main.html', context=context)


def categories(request):
    return render(request, 'main/categories.html')