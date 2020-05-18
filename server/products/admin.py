from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass
