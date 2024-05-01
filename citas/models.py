from django.db import models
from core.models import Profesional, Cliente # Importamos los modelos de la aplicación 'core' para usar Profesional y Cliente

class Cita(models.Model):
    """
        Este modelo establece los campos de Cita y las opciones del estado en el que pueden estar.
    """
    OPCIONES_ESTADO = (
        ('P', 'PENDIENTE'),
        ('A', 'ACEPTADA'),
        ('R', 'RECHAZADA')
    )
    
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField(null=False)
    precio = models.FloatField(null=False)
    estado = models.CharField(max_length=1, null=False, choices=OPCIONES_ESTADO)