from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.urls import reverse
from django.contrib import auth

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')  # Render the registration page if the request method is GET
    elif request.method == 'POST':
        username = request.POST.get('username')  # Get the username from the POST request
        email = request.POST.get('email')  # Get the email from the POST request
        senha = request.POST.get('senha')  # Get the password from the POST request
        confirmar_senha = request.POST.get('confirmar_senha')  # Get the password confirmation from the POST request

        # Check if passwords match
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Passwords do not match')
            return render(request, 'cadastro.html')

        # Check if password length is between 8 and 16 characters
        if not len(senha) >= 8 or len(senha) > 16:
            messages.add_message(request, constants.ERROR, 'Password must be between 8 and 16 characters long')
            return render(request, 'cadastro.html')

        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Email already exists')
            return render(request, 'cadastro.html')

        # Check if username is already in use
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Username already exists')
            return render(request, 'cadastro.html')

        # To do: Validate password strength

        # Create the new user
        criar_usuario = User.objects.create_user(
            username=username,
            email=email,
            password=senha,
        )
        criar_usuario.save()  # Save the new user to the database

        return redirect('login')  # Redirect to the login page after successful registration

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')  # Render the login page if the request method is GET
    elif request.method == 'POST':
        usuario = request.POST.get('username')  # Get the username from the POST request
        senha = request.POST.get('senha')  # Get the password from the POST request

        # Authenticate the user
        autenticar = auth.authenticate(username=usuario, password=senha)

        # Check if authentication failed
        if not autenticar:
            messages.add_message(request, constants.ERROR, 'Invalid username or password')
            return redirect('login')  # Redirect to the login page if authentication failed

        # Log the user in and redirect to the 'novo_evento' page
        auth.login(request, autenticar)
        return redirect('novo_evento')
