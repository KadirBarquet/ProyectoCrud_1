from django.db import models

class BaseModelo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre
    
class Marca(BaseModelo):
    pass

TALLA_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
]

class Producto(BaseModelo):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    talla = models.CharField(max_length=2, choices=TALLA_CHOICES)
    
    def __str__(self):
        return f"{self.nombre}"