from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo


class Producto(models.Model):
    """Entidad independiente usada para demostrar ORM y CRUD."""

    sku = models.CharField(max_length=20, primary_key=True, verbose_name="SKU")
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("nombre",)
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.sku} - {self.nombre}"


class ExistenciaSucursal(models.Model):
    """Entidad sin relaciones con una llave primaria compuesta (Django 6)."""

    pk = models.CompositePrimaryKey("codigo_sucursal", "sku_producto")
    codigo_sucursal = models.CharField(max_length=10)
    sku_producto = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "existencia por sucursal"
        verbose_name_plural = "existencias por sucursal"

    def __str__(self):
        return f"{self.codigo_sucursal}/{self.sku_producto}"
