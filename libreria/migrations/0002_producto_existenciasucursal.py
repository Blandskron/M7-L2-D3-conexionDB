from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('libreria', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='SKU')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos', 'ordering': ('nombre',)},
        ),
        migrations.CreateModel(
            name='ExistenciaSucursal',
            fields=[
                ('pk', models.CompositePrimaryKey('codigo_sucursal', 'sku_producto', blank=True, primary_key=True, serialize=False)),
                ('codigo_sucursal', models.CharField(max_length=10)),
                ('sku_producto', models.CharField(max_length=20)),
                ('cantidad', models.PositiveIntegerField(default=0)),
            ],
            options={'verbose_name': 'existencia por sucursal', 'verbose_name_plural': 'existencias por sucursal'},
        ),
    ]
