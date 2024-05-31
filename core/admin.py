from django.contrib import admin
from .models import Profesional, Especialidad

# Register your models here.

# Cargamos los modelos Profesional y Especialidad en el panel de administración de Django

admin.site.register(Profesional)
admin.site.register(Especialidad)
