# from django.shortcuts import render
# from .forms import TableroForm

# # Create your views here.

# def index2(request):
#     return render(request, 'tablero/index2.html', {})

# def tablero(request):
#     #SI SE HA ENVIADO EL FORMULARIO
#     if request.method == 'POST':
#         form = TableroForm(request.POST)
#         #EJECUTAMOS LA VALIDACIÓN
#         if form.is_valid():
#             #LOS DATOS SE COGEN DEL DICCIONARION CLEANED_DATA
#             filas = form.cleaned_data['filas']
#             columnas = form.cleaned_data['columnas']
#             tablero = index(filas, columnas)
#             return render(request, 'tablero/index.html', {'tablero': tablero})
#     else:
#         form = TableroForm()
#     return render(request, 'tablero/tablero_create.html', {'form': form})


# def index(filas, columnas):
#     tablero = [['' for _ in range(columnas)] for _ in range(filas)]
#     return tablero



# ////////////////////////

# import random

# from django.shortcuts import render
# from .forms import TableroForm

# def index2(request):
#     return render(request, 'tablero/index2.html', {})

# def tablero(request):
#     tablero = None  # Inicializamos tablero como nulo
#     minas = set()

#     if request.method == 'POST':
#         form = TableroForm(request.POST)

#         if form.is_valid():
#             filas = form.cleaned_data['filas']
#             columnas = form.cleaned_data['columnas']
#             num_minas = form.cleaned_data['num_minas']

#             total_casillas = filas * columnas
#             if num_minas <= total_casillas / 2:
#                 tablero = index(filas, columnas)
#                 return render(request, 'tablero/index.html', {'tablero': tablero})
#             else:
#                 form.add_error('num_minas', "El número de minas debe ser menor o igual a la mitad de las casillas del tablero.")
#         else:
#             # El formulario no es válido, lo renderizamos nuevamente con los errores
#             return render(request, 'tablero/tablero_create.html', {'form': form})
#     else:
#         form = TableroForm()

#     if tablero is not None:
#         # Si tablero se ha creado con éxito, mostramos la página "Muestra Tablero"
#         return render(request, 'tablero/index.html', {'tablero': tablero})
#     else:
#         # Si no se ha enviado el formulario o hay errores en el formulario, mostramos la página del formulario.
#         return render(request, 'tablero/tablero_create.html', {'form': form})

#     return render(request, 'tablero/tablero_create.html', {'form': form})

# def index(filas, columnas):
#     tablero = [['' for _ in range(columnas)] for _ in range(filas)]
#     return tablero

# ///////////////////////////////////

import random  # Importa el módulo random

from django.shortcuts import render
from .forms import TableroForm

def index2(request):
    return render(request, 'tablero/index2.html', {})

def tablero(request):
    tablero = None
    minas = set()  # Crea un conjunto para almacenar las coordenadas de las minas

    if request.method == 'POST':
        form = TableroForm(request.POST)

        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            num_minas = form.cleaned_data['num_minas']

            total_casillas = filas * columnas

            if num_minas <= total_casillas / 2:
                # Genera aleatoriamente las coordenadas de las minas y agrégalas al conjunto
                while len(minas) < num_minas:
                    fila = random.randint(0, filas - 1)
                    columna = random.randint(0, columnas - 1)
                    minas.add((fila, columna))

                tablero = index(filas, columnas, minas)
    else:
        form = TableroForm()

    if tablero is not None:
        return render(request, 'tablero/index.html', {'tablero': tablero})
    else:
        return render(request, 'tablero/tablero_create.html', {'form': form})

def index(filas, columnas, minas):
    tablero = [['' for _ in range(columnas)] for _ in range(filas)]
    
    # Modifica el tablero para marcar las casillas que son minas
    for fila, columna in minas:
        tablero[fila][columna] = 'M'  # Marca la casilla como mina
    
    return tablero
