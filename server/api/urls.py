from django.urls import path, include

urlpatterns = [
    path('carts/', include('carts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]
