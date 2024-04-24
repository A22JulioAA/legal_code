from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('usuarios/', include('usuarios.urls')),
    path('citas/', include('citas.urls')),
    path('comentarios/', include('comentarios.urls')),
]
