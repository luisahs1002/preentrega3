from django.db import models

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
    
