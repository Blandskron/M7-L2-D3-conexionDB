import random
from datetime import date
from libreria.models import Autor, Libro

autores = list(Autor.objects.all())
titulos_nuevos = [
    "El amor en los tiempos del cólera", "Relato de un náufrago", 
    "De amor y de sombra", "Inés del alma mía", "La biblioteca de Babel", 
    "El libro de arena", "62 Modelo para armar", "Historias de cronopios y de famas", 
    "La fiesta del Chivo", "Conversación en La Catedral"
]

for i, titulo in enumerate(titulos_nuevos):
    Libro.objects.create(
        titulo=titulo,
        fecha_publicacion=date(1970 + i, 5, 20),
        isbn=f"978111111111{i}",
        autor=random.choice(autores)
    )
