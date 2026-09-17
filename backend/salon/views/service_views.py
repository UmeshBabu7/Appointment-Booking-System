from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from salon.models import Service
from salon.serializers import ServiceSerializer


@api_view(["GET", "POST"])
def service_list(request):
    if request.method == "GET":
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def service_detail(request, id):
    service = get_object_or_404(Service, id=id)

    if request.method == "PUT":
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if service.appointments.exists():
        return Response(
            {"detail": "Cannot delete a service that has existing appointments."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    service.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
