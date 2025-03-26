from django.shortcuts import render, redirect
from .forms import SensorForm
from django.urls import reverse
from .models import Sensor, MedicionSensor
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from .serializer import SensorSerializer, MedicionSensorSerializer
from rest_framework import viewsets
# Create your views here.

def es_admin(user):
    return user.is_authenticated and user.is_staff

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()  # Recupera todos los sensores de la BD
    serializer_class = SensorSerializer

class MedicionSensorViewSet(viewsets.ModelViewSet):
    #queryset = MedicionSensor.objects.all()
    serializer_class = MedicionSensorSerializer

    def get_queryset(self):
        # Filtra las mediciones por el sensor_id en la URL
        sensor_id = self.kwargs['sensor_id']
        return MedicionSensor.objects.filter(sensor_id=sensor_id)

@login_required
@user_passes_test(es_admin)
def registro_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_sensores)
    else:
        form = SensorForm()
    return render(request, 'registro_sensor.html', {'form': form})

@login_required
def listar_sensores(request):
    sensores = Sensor.objects.all()  # Obtener todos los sensores de la base de datos
    return render(request, 'listar_sensores.html', {'sensores': sensores})

