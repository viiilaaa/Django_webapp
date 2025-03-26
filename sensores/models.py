from django.db import models

# Create your models here.

class Sensor(models.Model):
    
    id = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=100, unique=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    fecha_instalacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=(('activo', 'Activo'),('inactivo', 'Inactivo'),('mantenimiento', 'En Mantenimiento')), default='activo')
    
    def __str__(self):
        return f"Sensor {self.id} - ubicacion: {self.latitud}, {self.longitud} -> ({self.get_estado_display()})"

class MedicionSensor(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="mediciones")
    distancia = models.DecimalField(max_digits=5, decimal_places=2)  # Ajusta el tipo de dato según sea necesario
    fecha_medicion = models.DateTimeField()

    def __str__(self):
        return f"Medición Sensor {self.sensor.id} - Distancia: {self.distancia} - {self.fecha_medicion}"