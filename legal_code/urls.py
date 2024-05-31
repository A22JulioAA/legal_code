from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# Estas son las rutas que se van a usar en la aplicación. Se incluyen las rutas de los módulos core, citas, users y las rutas de autenticación de Django.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('citas/', include('citas.urls')),
    path('users/', include('users.urls')),
]

# Esto es simplemente una barra para debuguear la página.

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


