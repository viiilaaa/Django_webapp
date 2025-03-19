from django.db import models

# Create your models here.

class Sensor(models.Model):
    
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=255)
    fecha_instalacion = models.DateField()
    estado = models.CharField(max_length=20, choices=(('activo', 'Activo'),('inactivo', 'Inactivo'),('mantenimiento', 'En Mantenimiento')), default='activo')
    
    def __str__(self):
        return f"Sensor {self.id} - {self.ubicacion} ({self.get_estado_display()})"
