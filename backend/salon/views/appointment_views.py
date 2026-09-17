from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from salon.models import Appointment
from salon.serializers import (
    AppointmentSerializer,
)


@api_view(["GET", "POST"])
def appointment_list(request):
    if request.method == "GET":
        appointments = Appointment.objects.select_related("service").all()
        status_filter = request.query_params.get("status")
        if status_filter:
            appointments = appointments.filter(status__iexact=status_filter)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
