from django.db import models
from salon.models.service import Service


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        CONFIRMED = "Confirmed", "Confirmed"
        COMPLETED = "Completed", "Completed"
        CANCELLED = "Cancelled", "Cancelled"

    customer_name = models.CharField(max_length=150)
    customer_phone = models.CharField(max_length=30)
    service = models.ForeignKey(
        Service, on_delete=models.PROTECT, related_name="appointments"
    )
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date", "time"]
