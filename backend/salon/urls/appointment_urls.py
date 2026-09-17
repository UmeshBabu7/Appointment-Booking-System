from django.urls import path
from salon.views.appointment_views import appointment_list, appointment_detail


urlpatterns = [
    path("appointments", appointment_list, name="appointment-list"),
    path(
        "appointments/<int:pk>",
        appointment_detail,
        name="appointment-detail",
    ),
]
