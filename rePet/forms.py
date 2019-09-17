from django import forms
from rePet.models import Cadastro, Usuario

# Importando os campos da classe Cadastro na Models, que irão na página de Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'sobrenome',
            'email',
            'senha',
            'telefone',
            'endereco'
        ]

# Importando os campos da classe Usuario na Models, que irão na página de Login

class LoginUsuario(forms.ModelForm):
    email = Usuario
    senha = Usuario
    class Meta:
        model = Usuario
        fields = [
            'email',
            'senha'
        ]