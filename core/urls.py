from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

"""
En este array se almacenan las rutas que tendremos disponibles
En la aplicación. En cada una de ellas se establecen las relaciones 
con la vista creada para mostrar las plantillas en el fichero
views.py

"""

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('especialidad/<slug:filtro_especialidad>/', views.homepage, name='homepage_filtered'),
    path('subespecialidad/<slug:filtro_subespecialidad>/', views.homepage, name='homepage_double_filtered'),
    path('logout/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre-nosotros'),
    path('calendario/', views.calendario, name='calendario'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('obtener-citas/', views.obtener_citas, name='obtener_citas'),
    path('anular-cita/<int:id_cita>/', views.anular_cita, name='anular_cita'),
    path('politica-cancelaciones/', views.politica_cancelaciones, name='politica_cancelaciones'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

