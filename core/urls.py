from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profesionales/', views.profesionales, name='profesionales'),
    path('logout/', views.salir, name='salir')
]
