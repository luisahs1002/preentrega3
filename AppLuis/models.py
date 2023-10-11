from django.db import models
from django.contrib.auth.models import User 

class Piloto(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()

class Scuderia(models.Model):
    scuderia = models.CharField(max_length=60)

class Circuito(models.Model):
    circuito = models.CharField(max_length=60)
    tiempo = models.FloatField()

class Clasificacion(models.Model):
    nombre_apellido = models.CharField(max_length=60)
    circuito = models.CharField(max_length=60)
    tiempo = models.FloatField()

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
