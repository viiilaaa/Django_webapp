from django.urls import path
from .views import registro_sensor, listar_sensores

urlpatterns = [
    path('registrar/', registro_sensor, name='registro_sensor'),
    path('listar/', listar_sensores, name='listar_sensores'),
]