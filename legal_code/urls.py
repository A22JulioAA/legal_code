from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    # path('usuarios/', include('usuarios.urls')),
    # path('citas/', include('citas.urls')),
    # path('comentarios/', include('comentarios.urls')),
]
