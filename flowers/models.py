from django.db import models

# Create your models here.

class Flower(models.Model) :
    nombreflor = models.TextField(default='')
    tipo = models.TextField(default='', blank=True)
    color = models.TextField(default='')
    cantidad = models.FloatField(default=1.0)
    fecha = models.DateTimeField(default=0, blank=True)
    ocasion = models.TextField(default='')
    precio = models.FloatField(default=0.0)
    formadepago = models.TextField(default='')
    existencias = models.FloatField(default=0.0)
    direccion = models.TextField(blank=True)