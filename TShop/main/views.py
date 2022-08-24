from django.shortcuts import render
from .models import Products


# Create your views here.
def index(request):
    all_products = Products.objects.all()
    return render(request, 'main/main.html', {'prod_list': all_products})


def categories(request):
    return render(request, 'main/categories.html')