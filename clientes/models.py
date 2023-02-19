from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_aniversario = models.DateField()
    telefone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
