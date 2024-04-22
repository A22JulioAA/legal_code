from django.db import models
from usuarios.models import Profesional, Cliente # Importamos los modelos de la aplicación 'usuarios' para usar Profesional y Cliente

class Cita(models.Model):
    OPCIONES_ESTADO = (
        ('P', 'PENDIENTE'),
        ('A', 'ACEPTADA'),
        ('R', 'RECHAZADA')
    )
    
    profeisonal = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField(null=False)
    precio = models.FloatField(null=False)
    estado = models.CharField(max_length=1, null=False, choices=OPCIONES_ESTADO)