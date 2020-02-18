from django.urls import path, include
from .views import Shops

urlpatterns = [
    path('shops/<int:pk>/', Shops.as_view(), name='shops'),    
]