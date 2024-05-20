from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('eliminar-perfil/', views.eliminar_perfil, name='eliminar-perfil'),
]
