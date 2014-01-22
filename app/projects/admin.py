from django.contrib import admin

# Register your models here.
from projects.models import Proyecto,DatosPago

admin.site.register(Proyecto)
admin.site.register(DatosPago)