from django.urls import path
from .views import Fullpage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Fullpage.loginpage, name='index'),
    path("get_data/<str:owner>/", Fullpage.get_data, name='json'),
    # path("get_response", Fullpage.get_response, name='get_response'),
    path("73wyquihsah32okdshfjklqkdjai", Fullpage.matchpw, name="test")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
