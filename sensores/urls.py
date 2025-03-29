from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MedicionSensorViewSet

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/sensores/<int:sensor_id>/mediciones/', MedicionSensorViewSet.as_view({'get': 'list'}), name='mediciones'),
]