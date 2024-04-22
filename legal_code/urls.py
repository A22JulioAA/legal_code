from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('usuarios/', include('usuarios.urls')),
    path('citas/', include('citas.urls')),
    path('comentarios/', include('comentarios.urls')),
]
