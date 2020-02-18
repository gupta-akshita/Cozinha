from django.contrib import admin
from .models import Cart, CartItem, CartAdmin

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)


