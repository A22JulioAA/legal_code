from django.urls import path
from . import views

urlpatterns = [
    path('', views.citas_principal, name='citas-principal'),
    path('agendar-cita/', views.agendar_cita, name='agendar-cita'),
    path('agendar-cita/<int:id_profesional>/', views.agendar_cita, name='agendar-cita-info-profesional')
]