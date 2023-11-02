import random  # Importa el módulo random

from django.shortcuts import render
from .forms import TableroForm

from  .tablero import Casilla, Tablero

def index2(request):
    return render(request, 'tablero/index2.html', {})

def tablero(request):
    tablero = None

    if request.method == 'POST':
        form = TableroForm(request.POST)

        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            num_minas = form.cleaned_data['num_minas']

            total_casillas = filas * columnas

            if num_minas <= total_casillas / 2:
                # Crea una instancia de Tablero y genera el tablero con minas
                tablero = Tablero(filas, columnas, num_minas).mostrar_tablero()

    else:
        form = TableroForm()

    if tablero is not None:
        return render(request, 'tablero/index.html', {'form': form, 'tablero': tablero})
    else:
        return render(request, 'tablero/tablero_create.html', {'form': form})

