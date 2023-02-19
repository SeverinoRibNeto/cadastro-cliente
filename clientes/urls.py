from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_url, name='home_url'),
    path('cadastro/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('salvaCliente/', views.salva_cliente, name='salva_cliente'),
    path('alterarCliente/<int:id>', views.altera_cliente, name='altera_cliente'),
    path('atualiza_cliente/<int:id>',
         views.atualiza_cliente, name='atualiza_cliente'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente'),
    path('filtraCliente/',
         views.filtra_cliente, name='filtra_cliente'),
    path('excluirCliente/<int:id>', views.excluir_cliente, name='excluir_cliente')
]
