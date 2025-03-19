from django import forms
from .models import Sensor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['id','ubicacion', 'fecha_instalacion', 'estado']
        widgets = {
            'fecha_instalacion': forms.SelectDateWidget()
        }