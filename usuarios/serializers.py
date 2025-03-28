# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator
# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
# Models
from .models import UsuarioPersonalizado

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = UsuarioPersonalizado
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'rol'
        )

class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    username = serializers.CharField(min_length=4, max_length=20)
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
    

class UserSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=UsuarioPersonalizado.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=UsuarioPersonalizado.objects.all())]
    )

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)
    rol = serializers.ChoiceField(choices=[('admin', 'Administrador'), ('operador', 'Operador')])
    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = UsuarioPersonalizado.objects.create_user(**data)
        return user
