from django.urls import path
from . import views

urlpatterns = [
    path('crear_especialidad/', views.crear_especialidad, name='crear_especialidad'),
    path('eliminar_especialidad/', views.eliminar_especialidad, name='eliminar_especialidad'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('registro_cliente/', views.registro_cliente, name='registro'),
]