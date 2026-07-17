from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.producto_lista, name='producto_lista'),
    path('productos/nuevo/', views.producto_crear, name='producto_crear'),
    path('productos/<str:sku>/', views.producto_detalle, name='producto_detalle'),
    path('productos/<str:sku>/editar/', views.producto_editar, name='producto_editar'),
    path('productos/<str:sku>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('autores/', views.lista_autores, name='lista_autores'),
]
