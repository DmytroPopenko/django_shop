from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('categories/', views.categories, name="categories"),
    path('products/<slug:url_slug>/', views.product_view, name="product"),
]