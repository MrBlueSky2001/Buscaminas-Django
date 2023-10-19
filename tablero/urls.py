from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablero_create, name='tablero_create'),
]