from django.urls import path, include
from .views import SignUp, SignIn, LogOut
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('logout/', LogOut.as_view(), name='logout'),
    # path('signin/', ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
