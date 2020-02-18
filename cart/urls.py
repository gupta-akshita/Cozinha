from django.urls import path, include
from .views import AddToCart, CartView, GetData

urlpatterns = [
    path('updating', AddToCart.as_view(), name='updating' ),
    path('cart', CartView.as_view(), name='cart'),
    path('getting', GetData.as_view(), name='getting'),
    
]