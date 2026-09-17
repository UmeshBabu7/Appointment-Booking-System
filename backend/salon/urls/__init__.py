from django.urls import path, include

urlpatterns = [
    path("", include("salon.urls.service_urls")),
]