from django.urls import path
from . import views

"""
En este array se almacenan las rutas que tendremos disponibles
En la aplicación. En cada una de ellas se establecen las relaciones 
con la vista creada para mostrar las plantillas en el fichero
views.py

"""

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('especialidad/<slug:filtro_especialidad>/', views.homepage, name='homepage_filtered'),
    path('logout/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre-nosotros'),
    path('calendario/', views.calendario, name='calendario'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
]

