from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Pessoa


def home_url(request):
    pessoa = Pessoa.objects.last()
    return render(request, 'home.html', {'pessoa': pessoa})


def cadastrar_cliente(request):
    return render(request, 'cadastro.html')


def buscar_cliente(request):
    clientes = Pessoa.objects.all()
    return render(request, 'buscar.html', {'clientes': clientes})


def salva_cliente(request):
    pessoa = Pessoa()
    pessoa.nome = request.POST.get("nome")
    pessoa.sobrenome = request.POST.get("sobrenome")
    pessoa.data_aniversario = request.POST.get("aniversario")
    pessoa.email = request.POST.get("email")
    pessoa.endereco = request.POST.get("endereco")
    pessoa.telefone = request.POST.get("telefone")
    pessoa.save()
    return redirect(home_url)


def altera_cliente(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'atualizacao.html', {'pessoa': pessoa})


def atualiza_cliente(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = request.POST.get("nome")
    pessoa.sobrenome = request.POST.get("sobrenome")
    pessoa.data_aniversario = request.POST.get("aniversario")
    pessoa.email = request.POST.get("email")
    pessoa.endereco = request.POST.get("endereco")
    pessoa.telefone = request.POST.get("telefone")
    pessoa.save()
    return redirect(home_url)


def filtra_cliente(request):
    print(request.POST.get('filter_check'))
    if (str(request.POST.get('filter_check')) == 'id_check'):
        clientes = Pessoa.objects.filter(id=int(request.POST.get('find_text')))
    elif (str(request.POST.get('filter_check')) == 'nome_check'):
        clientes = Pessoa.objects.filter(
            nome__contains=str(request.POST.get('find_text')))
    elif (str(request.POST.get('filter_check')) == 'sobrenome_check'):
        clientes = Pessoa.objects.filter(
            sobrenome__contains=str(request.POST.get('find_text')))
    return render(request, 'buscar.html', {'clientes': clientes})


def excluir_cliente(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home_url)
