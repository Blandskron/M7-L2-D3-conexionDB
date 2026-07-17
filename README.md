# Librería educativa con Django y PostgreSQL

Proyecto simple para demostrar la conexión de Django a PostgreSQL, el ORM, entidades sin relaciones, claves primarias y operaciones CRUD.

## Ejecución con Docker

El único requisito es Docker. Desde la raíz del proyecto:

```bash
docker compose up --build
```

Luego abre:

- Aplicación y explicación: http://localhost:8000/
- CRUD de productos: http://localhost:8000/productos/
- API de libros: http://localhost:8000/api/libros/
- Administración: http://localhost:8000/admin/

Credenciales educativas del administrador: usuario `admin`, contraseña `admin1234`.

El contenedor espera a PostgreSQL y, cada vez que inicia, aplica migraciones, crea o actualiza el superusuario, carga datos de demostración de forma idempotente, recopila estáticos e inicia Django.

Para detenerlo:

```bash
docker compose down
```

Para eliminar también los datos persistidos y comenzar desde cero:

```bash
docker compose down -v
```

## Requisitos demostrados

- PostgreSQL configurado mediante variables de entorno en `proyecto/settings.py` y servicio `db` en Compose.
- `psycopg2-binary` declarado como controlador en `requirements.txt`.
- `Producto`: entidad independiente con campos de texto, decimal, entero positivo, booleano y fecha automática; usa `sku` como clave primaria simple y explícita.
- `ExistenciaSucursal`: entidad independiente con `CompositePrimaryKey` sobre `codigo_sucursal` y `sku_producto`.
- CRUD completo de `Producto`: crear, listar/leer, actualizar y eliminar mediante formularios, vistas, URLs y templates de Django.
- Validación de precio positivo, panel administrativo, datos iniciales y pruebas automatizadas.
- `Autor` y `Libro` conservan la funcionalidad original y sus endpoints JSON bajo `/api/`.

> Django no permite registrar modelos con `CompositePrimaryKey` en el panel admin. La clave compuesta se demuestra en el modelo, la migración, los datos iniciales y las pruebas; `Producto`, `Autor` y `Libro` sí están registrados en admin.

## Operaciones ORM para una demostración

```bash
docker compose exec web python manage.py shell
```

```python
from libreria.models import Producto

# Crear
p = Producto.objects.create(sku="DEM-001", nombre="Producto demo", precio=1000, stock=5)
# Leer
p = Producto.objects.get(pk="DEM-001")
# Actualizar
p.stock = 8
p.save()
# Borrar
p.delete()
```

## Verificación

Con los servicios activos:

```bash
docker compose exec web python manage.py check
docker compose exec web python manage.py migrate
docker compose exec web python manage.py test
docker compose config
```
