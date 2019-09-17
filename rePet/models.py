from django.db import models
from django.contrib.auth.models import User


# Classe para cadastrar os animais no site

class Animal(models.Model):

    animal_tamanho = [
        ('Porte Pequeno', 'Porte Pequeno'),
        ('Porte Médio', 'Porte Médio'),
        ('Porte Grande', 'Porte Grande'),
    ]

    animal_idade = [
        ('De 2 a 6 meses', 'De 2 a 6 meses'),
        ('1 ano', '1 ano'),
        ('2 anos', '2 anos'),
        ('3 anos', '3 anos'),
        ('4 anos', '4 anos'),
        ('5 anos', '5 anos'),
        ('6 anos', '6 anos'),
        ('7 anos', '7 anos'),
        ('8 anos', '8 anos'),
    ]
    nome = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=20, choices=animal_tamanho)
    idade = models.CharField(max_length= 20, choices=animal_idade)
    foto = models.ImageField(upload_to='')

    def __str__(self):
        return self.nome

# Classe para a página de cadastro do usuario

class Cadastro(models.Model):

    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Classe para a tela de login do usuario

class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome