from django.shortcuts import render

# Create your views here.

def tablero_create(request):
    return render(request, 'tablero/tablero_create.html', {})
