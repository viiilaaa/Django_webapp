
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    rol = models.CharField(max_length=50, choices=[('admin', 'Administrador'), ('operador', 'Operador')])

    def __str__(self):
        return self.username