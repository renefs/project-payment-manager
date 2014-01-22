from django.db import models

from django.contrib.auth.models import User

import moneyed
from djmoney.models.fields import MoneyField

# Create your models here.
class Proyecto(models.Model):

    BOOLEAN_CHOICES = (
        (1, "Yes"),
        (0, "No"),
    )

    cliente = models.ForeignKey(User)

    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()

    #precio = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    tiempo_estimado_en_minutos=models.FloatField(default=0)
    pagado = models.BooleanField(choices=BOOLEAN_CHOICES,default=0)
    numero_veces_descartado_por_cliente= models.IntegerField(default=0)
    cancelado = models.BooleanField(choices=BOOLEAN_CHOICES,default=0)
    eliminado = models.BooleanField(choices=BOOLEAN_CHOICES,default=0)

    def __unicode__(self):
        return "Proyecto {0} de {1}" .format(self.titulo, self.cliente.username)

class Tarea(models.Model):

    proyecto = models.ForeignKey(Proyecto)

    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    #porcentaje_completado=models.FloatField()
    tiempo = models.FloatField()


    def __unicode__(self):
          return "Tarea {0} de {1}" .format(self.titulo, self.proyecto)

class DatosPago(models.Model):

    proyecto = models.OneToOneField(Proyecto)
    cliente = models.OneToOneField(User)

    cantidad = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    fecha = models.DateTimeField()
    metodoPago = models.CharField(max_length=100)
    identificador = models.TextField()


