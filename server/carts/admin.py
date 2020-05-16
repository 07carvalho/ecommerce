from django.contrib import admin
from .models import *


@admin.register(Cart, CartItem)
class CartsAdmin(admin.ModelAdmin):
    pass
