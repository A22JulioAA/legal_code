from django.urls import path
from . import views

urlpatterns = [
    path('crear_comentario', views.crearComentario, name='crear_comentario')
]