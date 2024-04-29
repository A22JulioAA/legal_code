from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profesionales/', views.profesionales, name='profesionales'),
    path('logout/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('sobre-nosotros', views.sobre_nosotros, name='sobre-nosotros'),
]
