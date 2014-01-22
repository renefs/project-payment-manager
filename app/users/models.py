from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    datosFacturacion = models.ForeignKey('DatosFacturacion')

    #other fields here
    horas_disponibles=models.FloatField()
    website=models.URLField()

    def __unicode__(self):
        return "Perfil de %s" % self.user

class DatosFacturacion(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    cif_nif=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __unicode__(self):
          return "Datos de facturacion de %s" % self.first_name