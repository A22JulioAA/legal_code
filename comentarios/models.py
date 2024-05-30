from django.db import models
from core.models import Profesional # Importamos los modelos de la aplicación 'core' para usar Profesional
from users.models import Cliente
from django.utils import timezone

class Comentario(models.Model):
    """
    Modelo de comentarios de los clientes acerca de los profesionales
    Args:
        models (Model): Modelo principal del cual heredan

    """
    
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=False, related_name='comentarios')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, default=1)
    texto_comentario = models.TextField(max_length=400, default='')
    recomendacion = models.BooleanField(default=True)
    fecha_comentario = models.DateTimeField(null=False, default=timezone.now)
    valoracion = models.IntegerField(null=False, default=1)
    
    def __str__(self):
        return f"Comentario de {self.cliente} acerca de {self.profesional}"
    
