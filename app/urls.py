from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home.urls")),
] + static(settings.STATIC_URL)
