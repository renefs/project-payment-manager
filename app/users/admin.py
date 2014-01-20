from django.contrib import admin

# Register your models here.
from users.models import UserProfile, DatosFacturacion

admin.site.register(UserProfile)
admin.site.register(DatosFacturacion)