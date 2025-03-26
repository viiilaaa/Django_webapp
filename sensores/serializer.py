from rest_framework import serializers
from .models import Sensor, MedicionSensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'  

class MedicionSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicionSensor
        fields = ['sensor', 'distancia', 'fecha_medicion']
