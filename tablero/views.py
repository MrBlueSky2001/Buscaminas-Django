# Importa el módulo random
import random  

# Importa la función render desde el módulo shortcuts de Django
from django.shortcuts import render

# Importa la clase TableroForm desde el archivo forms.py en el mismo directorio
from .forms import TableroForm

# Importa las clases Casilla y Tablero desde el archivo tablero.py en el mismo directorio
from .tablero import Casilla, Tablero

# Vista para la página de inicio
def index2(request):
    # Renderiza la plantilla 'tablero/index2.html' sin ningún contexto
    return render(request, 'tablero/index2.html', {})

# Vista principal para la manipulación del tablero
def tablero(request):
    tablero = None

    # Verifica si la solicitud es de tipo POST
    if request.method == 'POST':
        # Crea una instancia del formulario TableroForm con los datos de la solicitud
        form = TableroForm(request.POST)

        # Verifica si el formulario es válido
        if form.is_valid():
            # Obtiene los datos limpios del formulario
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            num_minas = form.cleaned_data['num_minas']

            # Calcula el número total de casillas en el tablero
            total_casillas = filas * columnas

            # Verifica que el número de minas sea válido
            if num_minas <= total_casillas / 2:
                # Crea una instancia de la clase Tablero y genera el tablero con minas
                tablero = Tablero(filas, columnas, num_minas).mostrar_tablero()

    else:
        # Si la solicitud no es de tipo POST, crea una instancia vacía del formulario TableroForm
        form = TableroForm()

    # Verifica si se ha generado un tablero
    if tablero is not None:
        # Renderiza la plantilla 'tablero/index.html' con el formulario y el tablero como contexto
        return render(request, 'tablero/index.html', {'form': form, 'tablero': tablero})
    else:
        # Renderiza la plantilla 'tablero/tablero_create.html' con el formulario como contexto
        return render(request, 'tablero/tablero_create.html', {'form': form})


