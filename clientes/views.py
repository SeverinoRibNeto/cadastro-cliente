from django.shortcuts import render
from django.http import HttpResponse


def cadastrar_cliente(request):
    return render(request, 'cadastro.html')


def buscar_cliente(request):
    return render(request, 'buscar.html')
