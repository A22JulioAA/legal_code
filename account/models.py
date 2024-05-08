from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_cliente= models.BooleanField('Is Cliente', default=False)
    is_profesional = models.BooleanField('Is Profesional', default=False)
