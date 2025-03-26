from django.urls import path, include
from .views import registro_sensor, listar_sensores 
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MedicionSensorViewSet

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'sensores/(?P<sensor_id>\d+)/mediciones', MedicionSensorViewSet, basename='mediciones')

urlpatterns = [
    path('registrar/', registro_sensor, name='registro_sensor'),
    path('listar/', listar_sensores, name='listar_sensores'),
    path('api/', include(router.urls)),
]