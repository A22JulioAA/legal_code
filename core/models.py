from django.db import models

class Especialidad(models.Model):
    """
    Se crean los campos del modelo Especialidad

    Args:
        models (Model): Modelo principal del cual heredan

    """
    
    nombre = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.nombre
    

class Profesional(models.Model):
    """
    Se crean los campos del modelo Profesional
    
    Args:
        models (Model): Modelo principal del cual heredan

    """
    
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=200, null=False, unique=True) # email y password se escriben en inglés por comodidad y para evitar caracteres especiales
    password1 = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(null=False)
    dni = models.CharField(max_length=9, null=False, unique=True)
    telefono = models.CharField(max_length=20, null=False)
    especialidad = models.ManyToManyField(Especialidad, default="General")
    precio_consulta = models.FloatField()
    direccion = models.TextField()
    descripcion = models.TextField(max_length=450, default='')
    campo = models.CharField(max_length=50, default='Jurista')
    
    def __str__(self) -> str:
        return self.nombre + ' ' + self.apellidos 

class Cliente(models.Model):
    """
    Se crean los campos del modelo Cliente

    Args:
        models (Model): Modelo principal del cual heredan

    """
    
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=False, unique=True)
    password1 = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(null=False)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos 
    