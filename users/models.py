from typing import Any
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUserManager(UserManager):
    '''
    A custom user manager for managing user creation and authentication.

    Inherits from Django's UserManager class.
    '''

    def _create_user(self, email: str, password: str, **extra_fields: Any) -> Any:
        '''
        Crea un usuario con el email, contraseña y campos adicionales proporcionados.

        Args:
            email (str): El email del usuario
            password (str): La contraseña del usuario
            **extra_fields: Campos adicionales a guardar para el usuario

        Returns:
            Any: El usuario
        
        Raises:
            ValueError: Si no se proporciona un email
        '''
        if not email:
            raise ValueError('El email es obligatorio!')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        
        return usuario
    
    def create_user(self, email=None, password=None, **extra_field):
        '''
        Crea un usuario con el email, contraseña y campos adicionales proporcionados.

        Args:
            email (str): El email del usuario.
            password (str): La contraseña del usuario.
            **extra_fields: Campos adicionales a guardar para el usuario.

        Returns:
            Any: El usuario creado.
        '''
        extra_field.setdefault('is_staff', False)
        extra_field.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_field)

    def create_superuser(self, email=None, password=None, **extra_field):
        '''
        Crea un superusuario con el email, contraseña y campos adicionales proporcionados.

        Args:
            email (str): El email del usuario.
            password (str): La contraseña del usuario.
            **extra_fields: Campos adicionales a guardar para el usuario.

        Returns:
            Any: El superusuario creado.
        '''
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('name', 'admin')
        extra_field.setdefault('fecha_nacimiento', timezone.now())
        return self._create_user(email, password, **extra_field)

class Cliente(AbstractBaseUser, PermissionsMixin):
    """
    Se crean los campos del modelo Cliente

    Args:
        models (Model): Modelo principal del cual heredan

    """
    
    name = models.CharField('Nombre del usuario', max_length=100, null=False, blank=True)
    apellidos = models.CharField('Apellidos del usuario', max_length=100, null=True, blank=True)
    email = models.EmailField('Email del usuario', blank=True, max_length=254, null=False, unique=True)
    password = models.CharField('Contraseña', max_length=100, null=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento del usuario', null=True, blank=True)
    telefono = models.CharField('Teléfono del usuario', max_length=20, null=True, blank=True)
    imagen_perfil = models.ImageField('Imagen de perfil', upload_to='images/perfil/', height_field=None, width_field=None, max_length=200, default='images/perfil/default.jpg')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    lost_login = models.DateTimeField(blank = True, null = True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def get_full_name(self)->str:
        return self.name + self.apellidos
    def get_short_name(self)->str:
        return self.name or self.email.split('@')[0]
    
    
