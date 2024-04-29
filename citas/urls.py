from django.urls import path
from . import views

urlpatterns = [
    path('', views.citas_principal, name='citas-principal')
]