from django.urls import path
from salon.views.service_views import service_list, service_detail

urlpatterns = [
    path("services/", service_list, name="service-list"),
    path("services/<int:id>/", service_detail, name="service-detail"),
]
