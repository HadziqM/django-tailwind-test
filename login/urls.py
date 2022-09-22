from django.urls import path
from .views import Fullpage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Fullpage.loginpage, name='index'),
    path("getpost", Fullpage.matchpw, name="test")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
