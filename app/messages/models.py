from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Mensaje(models.Model):

    emisor = models.ForeignKey(User,related_name='user_emisor')
    receptor = models.ForeignKey(User,related_name='user_receptor')

    texto=models.TextField()
    fecha = models.DateTimeField()