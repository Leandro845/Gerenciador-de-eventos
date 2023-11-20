from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.urls import reverse
from django.contrib import auth


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não conferem')
            return render(request, 'cadastro.html')

        if not len(senha) >= 8 or len(senha) > 16:
            messages.add_message(request, constants.ERROR,
                                 'A senha tem que ter no minímo 8 caracteres e no máximo 16'
                                 )
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Email já existente')
            return render(request, 'cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário já existente')
            return render(request, 'cadastro.html')

        # To do: Validar a força da senha

        criar_usuario = User.objects.create_user(
            username=username,
            email=email,
            password=senha,
        )
        criar_usuario.save()

        return redirect('login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')

        autenticar = auth.authenticate(username=usuario, password=senha)

        if not autenticar:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('login')

        auth.login(request, autenticar)
        return redirect('novo_evento')

