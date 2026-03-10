import os
import django
import random
from datetime import date

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
django.setup()

from libreria.models import Autor, Libro

def run_seed():
    # Limpiar datos existentes
    Libro.objects.all().delete()
    Autor.objects.all().delete()

    # Crear Autores
    autores_nombres = [
        "Gabriel García Márquez", "Isabel Allende", "Jorge Luis Borges", 
        "Julio Cortázar", "Mario Vargas Llosa"
    ]
    
    objetos_autores = []
    for nombre in autores_nombres:
        autor = Autor.objects.create(nombre=nombre, biografia=f"Biografía de {nombre}")
        objetos_autores.append(autor)

    # Crear 10 Libros
    titulos = [
        "Cien años de soledad", "La casa de los espíritus", "El Aleph", 
        "Rayuela", "La ciudad y los perros", "Crónica de una muerte anunciada", 
        "Eva Luna", "Ficciones", "Bestiario", "Pantaleón y las visitadoras"
    ]

    for i in range(10):
        Libro.objects.create(
            titulo=titulos[i],
            fecha_publicacion=date(1960 + i, 1, 1),
            isbn=f"978000000000{i}",
            autor=random.choice(objetos_autores)
        )

if __name__ == '__main__':
    run_seed()