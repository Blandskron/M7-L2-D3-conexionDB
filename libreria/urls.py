from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('autores/', views.lista_autores, name='lista_autores'),
]