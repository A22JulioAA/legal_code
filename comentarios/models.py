from django.db import models
from usuarios.models import Profesional, Cliente # Importamos los modelos de la aplicación 'usuarios' para usar Profesional y Cliente
from datetime import datetime

class Comentario(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=False, default=1)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, default=1)
    texto_comentario = models.TextField(max_length=400, default='')
    recomendacion = models.BooleanField(default=True)
    fecha_comentario = models.DateTimeField(null=False, default=datetime.now())
    valoracion = models.IntegerField(null=False, default=1)
    

