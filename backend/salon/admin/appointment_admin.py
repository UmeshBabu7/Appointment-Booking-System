from django.contrib import admin
from salon.models.appointment import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_name", "service", "date", "time", "status"]
    list_filter = ["status", "date", "service"]
