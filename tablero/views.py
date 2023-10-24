from django.shortcuts import render
from .forms import TableroForm

# Create your views here.

def index2(request):
    return render(request, 'tablero/index2.html', {})

def tablero(request):
    if request.method == 'GET':
        form = TableroForm(request.GET)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            tablero = index(filas, columnas)
            return render(request, 'tablero/index.html', {'tablero': tablero})
    else:
        form = TableroForm()
    return render(request, 'tablero/tablero_create.html', {'form': form})


def index(filas, columnas):
    tablero = [['' for _ in range(columnas)] for _ in range(filas)]
    return tablero



#def tablero_create(request):
#    return render(request, 'tablero/tablero_create.html', {})


