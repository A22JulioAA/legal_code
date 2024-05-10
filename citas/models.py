from django.db import models
from core.models import Profesional # Importamos los modelos de la aplicación 'core' para usar Profesional
from users.models import Cliente

class Cita(models.Model):
    """
        Este modelo establece los campos de Cita y las opciones del estado en el que pueden estar.
    """
    OPCIONES_ESTADO = (
        ('P', 'PENDIENTE'),
        ('E', 'ESPERA'),
        ('C', 'CANCELADA')
    )
    
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField(null=False)
    precio = models.FloatField(null=False)
    estado = models.CharField(max_length=1, null=False, choices=OPCIONES_ESTADO)
    descripcion = models.TextField(max_length=400, null=True, default='')

    def __str__(self):
        return self.cliente.name + ' - ' + self.estado