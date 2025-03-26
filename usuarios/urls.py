from django.urls import path, include
from .views import registro, inicio_sesion, home, logout_view
from rest_framework.routers import DefaultRouter

# Views
from usuarios import views as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', inicio_sesion, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('', include(router.urls))
]