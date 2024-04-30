from django.urls import path
from . import views

# Aquí se establecen las urls a las que el usuario va a poder acceder con sus respectivas
# views. Estas son las páginas principales o las que no cuentan con una profunda complejidad
# en su estructura de datos. Por el contrario, existen otras urls más complejas que se tratan
# en aplicaciones individuales y se crean paths independientes.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profesionales/', views.profesionales, name='profesionales'),
    path('logout/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre-nosotros'),
    path('calendario/', views.calendario, name='calendario'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
]
