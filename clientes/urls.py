from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('buscar/', views.buscar_cliente, name='buscar_cliente')
]
