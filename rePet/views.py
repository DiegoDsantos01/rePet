from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rePet.models import Animal, Cadastro, Usuario
from rePet.forms import CadastroForm, LoginUsuario



# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_adote(request):
    animais = Animal.objects.all()
    return render(request, 'adote.html', {'animais': animais})

def mostrar_cadastro(request):
    cad = Cadastro.objects.all()
    formulario = CadastroForm(request.POST or None)
    msg =''

    if formulario.is_valid():
        formulario.save()
        formulario = CadastroForm()
        msg = 'Cadastro realizado com sucesso'
    
    contexto = {
        'form': formulario,
        'msg': msg,
    }
    return render(request, 'cadastro.html')


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos. Tente novamente.')
    return redirect('/login/')
   

