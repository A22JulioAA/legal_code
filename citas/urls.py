from django.urls import path
from . import views

# Las URLs de la aplicación citas que luego se incluirán en las URLs globales del proyecto

urlpatterns = [
    path('', views.citas_principal, name='citas-principal'),
    path('agendar-cita/', views.agendar_cita, name='agendar-cita'),
    path('agendar-cita/<int:id_profesional>/', views.agendar_cita, name='agendar-cita-info-profesional')
]