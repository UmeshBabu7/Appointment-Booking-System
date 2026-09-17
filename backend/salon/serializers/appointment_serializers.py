from rest_framework import serializers
from salon.models.appointment import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service.name", read_only=True)
    service_price = serializers.DecimalField(
        source="service.price", max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "customer_name",
            "customer_phone",
            "service",
            "service_name",
            "service_price",
            "date",
            "time",
            "notes",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["status", "created_at", "updated_at"]

    def validate_customer_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Customer name cannot be empty.")
        return value

    def validate_customer_phone(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Customer phone cannot be empty.")
        return value


