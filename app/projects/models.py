from django.db import models

from django.contrib.auth.models import User

import moneyed
from djmoney.models.fields import MoneyField

# Create your models here.
class Proyecto(models.Model):
    user = models.ForeignKey(User)

    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()

    precio = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    tiempo_estimado_en_minutos=models.IntegerField()
    pagado = models.BooleanField()
    numero_veces_descartado_por_cliente= models.IntegerField()
    cancelado = models.BooleanField()
    eliminado = models.BooleanField()

    def __unicode__(self):
        return "Proyecto % de %s" % self.titulo % self.user

class Tarea(models.Model):

    proyecto = models.ForeignKey(Proyecto)

    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    porcentaje_completado=models.FloatField()
    tiempo = models.TimeField()


    def __unicode__(self):
          return "Tarea %s de %s" % self.titulo % self.proyecto

class DatosPago(models.Model):

    proyecto = models.OneToOneField(Proyecto)
    cliente = models.OneToOneField(User)

    cantidad = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    fecha = models.DateTimeField()
    metodoPago = models.CharField(max_length=100)
    identificador = models.TextField()


