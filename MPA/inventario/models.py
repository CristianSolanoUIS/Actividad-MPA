from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=30)
    fecha_creacion = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre


class Cambio_Stock(models.Model):
    INGRESO = 'Ingreso'
    EGRESO = 'Egreso'
    TIPO_CAMBIO_CHOICES = [(INGRESO, 'Ingreso'),(EGRESO, 'Egreso'),]
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo_cambio = models.CharField(max_length= 10, choices=TIPO_CAMBIO_CHOICES)
    comentario = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.id_producto.nombre

    

