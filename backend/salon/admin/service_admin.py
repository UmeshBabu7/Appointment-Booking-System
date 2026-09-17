from django.contrib import admin
from salon.models.service import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "duration"]
    list_filter = ["name"]
