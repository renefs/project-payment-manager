__author__ = 'rene'

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField, CurrencyField

class Compra(models.Model):

    BOOLEAN_CHOICES = (
        (1, "Yes"),
        (0, "No"),
    )

    cliente = models.ForeignKey(User)

    fecha_compra=models.DateTimeField()
    is_carrito=models.BooleanField(choices=BOOLEAN_CHOICES,default=1)

    precio_total=MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

class Cupon(models.Model):

    CUPON_CHOICES = (
        ("cantidad", "Descontar cantidad"),
        ("porcentaje", "Descontar porcentaje (%)"),
    )

    BOOLEAN_CHOICES = (
        (1, "Yes"),
        (0, "No"),
    )

    tipo = models.BooleanField(choices=CUPON_CHOICES,default="cantidad")
    cantidad = models.FloatField()
    #combinable_con_otros_cupones = models.BooleanField(choices=BOOLEAN_CHOICES,default=0)
    aplicable_pedidos_mayores = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    limite_de_usos = models.IntegerField(default=1)
    fecha_vencimiento=models.DateField()
    is_active= models.BooleanField(choices=BOOLEAN_CHOICES,default=1)

class DatosPago(models.Model):

    nombre = models.TextField(max_length=100,unique=True)

    compra = models.ForeignKey(Compra)
    cupon = models.ForeignKey(Cupon)

    moneda = CurrencyField()
    fecha_pago = models.DateTimeField()
    metodoPago = models.CharField(max_length=50)
    identificador_transaccion = models.CharField(max_length=100)
    precio_pagado = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    iva = models.FloatField()
    identificador = models.CharField(max_length=100)

class ProductoVendido(models.Model):

    compra = models.ForeignKey(Compra)
    producto_referencia = models.ForeignKey(Producto)

    nombre = models.CharField(max_length=100)
    unidades_compradas = models.IntegerField()
    precio_venta_unidad = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

    iva = models.FloatField()


