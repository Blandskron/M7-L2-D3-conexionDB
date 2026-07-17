from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import ExistenciaSucursal, Producto


class ProductoCRUDTests(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(sku='LAP-01', nombre='Laptop', precio=Decimal('799.90'), stock=3)

    def test_paginas_principales_responden(self):
        for url in (reverse('inicio'), reverse('producto_lista'), reverse('producto_detalle', args=[self.producto.pk]), '/admin/login/'):
            self.assertEqual(self.client.get(url).status_code, 200)

    def test_crear_actualizar_y_eliminar_producto(self):
        datos = {'sku': 'TEC-01', 'nombre': 'Teclado', 'descripcion': '', 'precio': '25.50', 'stock': 4, 'activo': True}
        self.assertEqual(self.client.post(reverse('producto_crear'), datos).status_code, 302)
        producto = Producto.objects.get(pk='TEC-01')
        datos.update(nombre='Teclado mecánico')
        self.client.post(reverse('producto_editar', args=[producto.pk]), datos)
        producto.refresh_from_db()
        self.assertEqual(producto.nombre, 'Teclado mecánico')
        self.client.post(reverse('producto_eliminar', args=[producto.pk]))
        self.assertFalse(Producto.objects.filter(pk='TEC-01').exists())

    def test_rechaza_precio_no_positivo(self):
        response = self.client.post(reverse('producto_crear'), {'sku': 'X', 'nombre': 'X', 'precio': '0', 'stock': 0})
        self.assertContains(response, 'El precio debe ser mayor que cero.')


class LlaveCompuestaTests(TestCase):
    def test_crear_y_leer_por_llave_compuesta(self):
        ExistenciaSucursal.objects.create(codigo_sucursal='STGO', sku_producto='LAP-01', cantidad=7)
        existencia = ExistenciaSucursal.objects.get(pk=('STGO', 'LAP-01'))
        self.assertEqual(existencia.cantidad, 7)

# Create your tests here.
