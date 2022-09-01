from django.contrib import admin

# Register your models here.
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'stock', 'time_create', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ['title']


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories)
