from django.utils.timezone import now
from django.shortcuts import render, redirect
from .forms import SensorForm
from .models import Sensor, MedicionSensor
from django.contrib.auth.decorators import login_required, user_passes_test
from .serializer import SensorSerializer, MedicionSensorSerializer
from rest_framework import viewsets, mixins, status

from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsStandardUser
from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
# Create your views here.
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()  # Recupera todos los sensores de la BD
    serializer_class = SensorSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

class MedicionSensorViewSet(viewsets.ModelViewSet):
    #queryset = MedicionSensor.objects.all()
    serializer_class = MedicionSensorSerializer

    def get_queryset(self):
        # Filtra las mediciones por el sensor_id en la URL
        sensor_id = self.kwargs['sensor_id']
        return MedicionSensor.objects.filter(sensor_id=sensor_id)
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        """Filtra mediciones por sensor_id y rango de fechas."""
        sensor_id = self.kwargs.get('sensor_id')
        fecha_inicio = request.GET.get("fecha_inicio")
        fecha_fin = request.GET.get("fecha_fin", now().isoformat())  # Si no se da fecha_fin, se usa la fecha actual

        if not fecha_inicio:
            return Response({"error": "Se requiere el parámetro fecha_inicio"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Convertir las fechas a objetos datetime
        fecha_inicio = parse_datetime(fecha_inicio)
        fecha_fin = parse_datetime(fecha_fin)

        if not fecha_inicio or not fecha_fin:
            return Response({"error": "Formato de fecha inválido. Usa YYYY-MM-DDTHH:MM:SSZ"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Filtrar las mediciones
        mediciones = MedicionSensor.objects.filter(sensor_id=sensor_id, fecha_medicion__range=(fecha_inicio, fecha_fin))
        
        serializer = MedicionSensorSerializer(mediciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
