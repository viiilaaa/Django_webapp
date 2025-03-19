from django.urls import path
from .views import registro_sensor, listar_sensores, mostrar_dato_sensor

urlpatterns = [
    path('registrar/', registro_sensor, name='registro_sensor'),
    path('listar/', listar_sensores, name='listar_sensores'),
    path('data/', mostrar_dato_sensor, name='data'),

]