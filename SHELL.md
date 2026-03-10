## 🛠️ Guía de Operaciones en Django Shell

La **Django Shell** es un entorno interactivo de Python que carga toda la configuración de tu proyecto, permitiéndote interactuar con tus modelos (`Autor` y `Libro`) usando el **ORM (Object-Relational Mapper)** de Django.

### 1. Acceso al Entorno

Para iniciar la consola interactiva, asegúrate de tener el entorno virtual activo y ejecuta:

```bash
python manage.py shell

```

### 2. Importación de Modelos

Antes de cualquier operación, debes importar tus clases en la sesión de la shell:

```python
from libreria.models import Autor, Libro

```

---

### 3. Referencia de Operaciones CRUD

#### **A. Creación de Registros (Create)**

Existen dos formas principales de añadir datos:

* **Método `.create()`:** Crea y guarda en un solo paso.
```python
nuevo_autor = Autor.objects.create(nombre="Bastian", biografia="Desarrollador de software")

```


* **Instancia manual:** Útil si necesitas procesar datos antes de guardar.
```python
libro = Libro(titulo="Django Master", isbn="1234567890123", autor=nuevo_autor, fecha_publicacion="2026-03-10")
libro.save()

```



#### **B. Consultas y Lectura (Read)**

El motor de búsqueda de Django es potente y flexible:

* **Recuperar todo:** `Libro.objects.all()`
* **Búsqueda exacta:** `Libro.objects.get(isbn="1234567890123")` *(Lanza error si no existe)*.
* **Filtrado avanzado:**
* `Libro.objects.filter(titulo__icontains="Django")` (Busca coincidencias parciales).
* `Libro.objects.filter(autor__nombre="Bastian")` (Filtra por campos del modelo relacionado).



#### **C. Actualización (Update)**

Para modificar datos, primero recuperas el objeto, cambias sus atributos y guardas:

```python
autor = Autor.objects.get(nombre="Bastian")
autor.biografia = "Especialista en Python y Django"
autor.save()

```

#### **D. Eliminación (Delete)**

Puedes eliminar un objeto individual o un conjunto de resultados:

* **Individual:** `Autor.objects.get(id=1).delete()`
* **Masivo:** `Libro.objects.filter(fecha_publicacion__year=2020).delete()`

> **Importante:** Debido a `on_delete=models.CASCADE` en tu modelo `Libro`, si eliminas un **Autor**, todos sus **Libros** asociados se borrarán automáticamente.

---

### 4. Resumen de Comandos de Utilidad

| Objetivo | Comando ORM |
| --- | --- |
| **Contar registros** | `Libro.objects.count()` |
| **Ordenar resultados** | `Libro.objects.order_by('titulo')` |
| **Limitar resultados** | `Libro.objects.all()[:5]` (Primeros 5) |
| **Ver SQL generado** | `print(Libro.objects.all().query)` |
