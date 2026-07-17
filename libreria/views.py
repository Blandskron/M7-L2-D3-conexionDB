from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProductoForm
from .models import Autor, Libro, Producto


def inicio(request):
    return render(request, 'libreria/inicio.html')

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


def producto_lista(request):
    return render(request, 'libreria/producto_lista.html', {'productos': Producto.objects.all()})


def producto_detalle(request, sku):
    producto = get_object_or_404(Producto, pk=sku)
    return render(request, 'libreria/producto_detalle.html', {'producto': producto})


def producto_crear(request):
    form = ProductoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        producto = form.save()
        return redirect('producto_detalle', sku=producto.pk)
    return render(request, 'libreria/producto_form.html', {'form': form, 'titulo': 'Crear producto'})


def producto_editar(request, sku):
    producto = get_object_or_404(Producto, pk=sku)
    form = ProductoForm(request.POST or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('producto_detalle', sku=producto.pk)
    return render(request, 'libreria/producto_form.html', {'form': form, 'titulo': 'Editar producto'})


def producto_eliminar(request, sku):
    producto = get_object_or_404(Producto, pk=sku)
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('producto_lista'))
    return render(request, 'libreria/producto_confirmar_eliminar.html', {'producto': producto})
