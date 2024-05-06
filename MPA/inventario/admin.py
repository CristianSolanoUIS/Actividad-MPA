from django.contrib import admin
from .models import Producto, Cambio_Stock 

# Register your models here.

admin.site.register(Producto)
admin.site.register(Cambio_Stock)