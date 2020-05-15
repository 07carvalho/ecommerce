from django.contrib import admin
from django.urls import path, include
from api.views import product

urlpatterns = [
    path('products/', product.ProductList.as_view(), name='product_list'),
    path('products/<int:product_id>/', product.ProductDetail.as_view(), name='product_detail'),
]