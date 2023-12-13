# Importa la clase path desde el módulo urls de Django
from django.urls import path

# Importa las vistas desde el módulo views en el mismo directorio
from . import views

# Lista de patrones de URL para la aplicación
urlpatterns = [
    # Asocia la vista index2 a la ruta principal ('')
    path('', views.index2, name='index2'),

    # Asocia la vista tablero a la ruta 'index'
    path('index', views.tablero, name='tablero_create'),
]
