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