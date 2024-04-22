from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.nombre
    

class Profesional(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, default='-')
    email = models.EmailField(max_length=200, null=False, unique=True) # email y password se escriben en inglés por comodidad y para evitar caracteres especiales
    password = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(null=False)
    dni = models.CharField(max_length=9, null=False, unique=True)
    telefono = models.CharField(max_length=20, null=False)
    especialidad = models.ManyToManyField(Especialidad, default="General")
    precio_consulta = models.FloatField()
    direccion = models.TextField()
    
    def __str__(self) -> str:
        return self.nombre + self.apellidos + '\ Email: ' + self.email

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(null=False)
    telefono = models.CharField(max_length=20)