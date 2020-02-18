from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import products

urlpatterns = [
    # path('', include('products.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)