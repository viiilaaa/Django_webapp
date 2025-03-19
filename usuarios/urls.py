from django.urls import path
from .views import registro, inicio_sesion, home, logout_view

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', inicio_sesion, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
]