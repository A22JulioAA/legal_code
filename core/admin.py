from django.contrib import admin
from .models import Cliente, Profesional, Especialidad

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Profesional)
admin.site.register(Especialidad)
