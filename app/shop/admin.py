__author__ = 'rene'

from django.contrib import admin

from shop.models import *

# Register your models here.
admin.site.register(Cupon)
admin.site.register(Compra)
admin.site.register(DatosPago)
admin.site.register(ProductoVendido)
admin.site.register(Producto)