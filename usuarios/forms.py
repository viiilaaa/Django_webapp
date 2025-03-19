from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'rol']
