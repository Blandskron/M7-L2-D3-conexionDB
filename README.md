# Tutorial: Creación de API de Librería con Django (JSON)

Este tutorial guía el proceso de creación de una aplicación Django para gestionar **Autores** y **Libros** con una relación de uno a muchos, diseñada para responder exclusivamente en formato JSON.

## 1. Configuración del Entorno y Proyecto

Ejecuta los siguientes comandos en tu terminal para preparar el entorno:

```bash
python -m venv venv
source venv/Scripts/activate  # En Windows: venv\Scripts\activate
pip install django
django-admin startproject proyecto .
django-admin startapp libreria

```

## 2. Definición de Modelos (`models.py`)

Define la estructura de datos en `libreria/models.py`:

```python
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

```

## 3. Vistas JSON (`views.py`)

Configura las respuestas automáticas en formato JSON en `libreria/views.py`:

```python
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Libro, Autor

def lista_libros(request):
    libros = list(Libro.objects.values('id', 'titulo', 'fecha_publicacion', 'isbn', 'autor__nombre'))
    return JsonResponse({'libros': libros}, safe=False)

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    data = {
        'id': libro.id,
        'titulo': libro.titulo,
        'fecha_publicacion': libro.fecha_publicacion,
        'isbn': libro.isbn,
        'autor': libro.autor.nombre
    }
    return JsonResponse(data)

def lista_autores(request):
    autores = list(Autor.objects.values('id', 'nombre', 'biografia'))
    return JsonResponse({'autores': autores}, safe=False)

```

## 4. Configuración de Rutas (`urls.py`)

Crea el archivo `libreria/urls.py` y conéctalo:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('autores/', views.lista_autores, name='lista_autores'),
]

```

*Nota: No olvides incluir `path('', include('libreria.urls'))` en el `urls.py` principal del proyecto.*

## 5. Migraciones y Base de Datos

Aplica los cambios a la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

## 6. Carga de Datos Iniciales (`seed_info.py`)

Crea un archivo en la raíz llamado `seed_info.py` para poblar la base de datos automáticamente con 10 libros y 5 autores:

```python
# Ejecutar con: python seed_info.py
import os, django, random
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
django.setup()

from libreria.models import Autor, Libro

# Lógica de creación de objetos...
# (Copia aquí el código de seed proporcionado anteriormente)

```

## 7. Gestión vía Shell

Para añadir 10 libros más o realizar consultas rápidas, usa la terminal de Django:

```bash
python manage.py shell

```

**Comandos útiles:**

* `Libro.objects.all()`: Ver todos los libros.
* `Libro.objects.filter(titulo__icontains="amor")`: Buscar por palabra clave.

## 8. Ejecución

Inicia el servidor de desarrollo:

```bash
python manage.py runserver

```

Accede a `http://127.0.0.1:8000/libros/` para ver los resultados en JSON.
