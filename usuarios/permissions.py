from rest_framework.permissions import BasePermission

# Models
from .models import UsuarioPersonalizado


class IsStandardUser(BasePermission):
    """Allow access to create experience, extras and proyects."""

    def has_permission(self, request, view):

        try:
            user = UsuarioPersonalizado.objects.get(
                username=request.user.username,
                is_active=True
            )
        except UsuarioPersonalizado.DoesNotExist:
            return False
        return True