from decimal import Decimal

from django.core.management.base import BaseCommand

from libreria.models import ExistenciaSucursal, Producto


class Command(BaseCommand):
    help = 'Crea datos mínimos e idempotentes para demostrar el ORM.'

    def handle(self, *args, **options):
        productos = [
            ('LIB-001', 'Cuaderno universitario', Decimal('3490.00'), 25),
            ('LIB-002', 'Set de lápices', Decimal('1990.00'), 40),
        ]
        for sku, nombre, precio, stock in productos:
            Producto.objects.get_or_create(sku=sku, defaults={'nombre': nombre, 'precio': precio, 'stock': stock})
        ExistenciaSucursal.objects.get_or_create(
            codigo_sucursal='STGO', sku_producto='LIB-001', defaults={'cantidad': 25}
        )
        self.stdout.write(self.style.SUCCESS('Datos de demostración disponibles.'))
