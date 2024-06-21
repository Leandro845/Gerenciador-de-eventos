from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Evento, Certificado  # Importing models Evento and Certificado
from django.contrib import messages  # Importing messages framework
from django.contrib.messages import constants  # Importing message constants
from django.http import Http404  # Importing Http404 exception
import csv  # Importing CSV module for CSV operations
from secrets import token_urlsafe  # Importing token_urlsafe from secrets module
from django.conf.urls.static import settings  # Importing Django settings for static files
import os  # Importing os module for system-level operations
from io import BytesIO  # Importing BytesIO for in-memory file operations
from django.core.files.uploadedfile import InMemoryUploadedFile  # Importing InMemoryUploadedFile for file uploads
from PIL import Image, ImageDraw, ImageFont  # Importing PIL modules for image processing
import sys  # Importing sys module for system-specific parameters and functions
from django.urls import reverse  # Importing reverse function from Django URLs

@login_required
def novo_evento(request):
    """View function for creating a new event."""
    if request.method == 'GET':
        return render(request, 'novo_evento.html')  # Render the form to create a new event
    elif request.method == 'POST':
        # Extract data from POST request
        nome_evento = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        data_inicio = request.POST.get('data_inicio')
        data_termino = request.POST.get('data_termino')
        carga_horaria = request.POST.get('carga_horaria')
        logo = request.FILES.get('logo')

        cor_principal = request.POST.get('cor_principal')
        cor_secundaria = request.POST.get('cor_secundaria')
        cor_fundo = request.POST.get('cor_fundo')

        # Create new Evento object and save to database
        evento = Evento(
            criador=request.user,
            nome=nome_evento,
            descricao=descricao,
            data_inicio=data_inicio,
            data_termino=data_termino,
            carga_horario=carga_horaria,
            logo=logo,
            cor_principal=cor_principal,
            cor_secundaria=cor_secundaria,
            cor_fundo=cor_fundo
        )
        evento.save()

        # Add success message and redirect to the same page
        messages.add_message(request, constants.SUCCESS, 'Event created successfully')
        return redirect('novo_evento')

@login_required
def gerenciar_evento(request):
    """View function for managing events."""
    if request.method == 'GET':
        nome = request.GET.get('nome')

        eventos = Evento.objects.filter(criador=request.user)

        # TODO: Add additional filters
        
        if nome:
            eventos = eventos.filter(nome__contains=nome)

        return render(request, 'gerenciar_evento.html', {'eventos': eventos})

@login_required
def inscrever_evento(request, id):
    """View function for registering for an event."""
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'GET':
        return render(request, 'inscrever_evento.html', {'evento': evento})
    elif request.method == 'POST':
        # Add current user to event participants and save
        evento.participantes.add(request.user)
        evento.save()
        messages.add_message(request, constants.SUCCESS, 'Registration successful')
        return redirect('inscricao_realizada')

def inscricao_realizada(request):
    """View function for displaying registration success."""
    return render(request, 'inscricao_realizada.html')

def participantes_evento(request, id):
    """View function for displaying participants of an event."""
    evento = get_object_or_404(Evento, id=id)
    if evento.criador == request.user:
        if request.method == 'GET':
            participantes = evento.participantes.all()
            return render(request, 'participantes_eventos.html',
                          {'participantes': participantes, 'evento': evento})
    else:
        raise Http404('This event is not yours')

def gerar_csv(request, id):
    """View function for generating a CSV file of event participants."""
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('This event is not yours')
    participantes = evento.participantes.all()

    # Generate a unique token for the CSV file
    token = f'{token_urlsafe(6)}.csv'
    path = os.path.join(settings.MEDIA_ROOT, token)

    # Write participants' data to CSV file
    with open(path, 'w') as arq:
        writer = csv.writer(arq, delimiter=",")
        for participante in participantes:
            data_row = (participante.username, participante.email)
            writer.writerow(data_row)

    return redirect(f'/media/{token}')

def certificados_evento(request, id):
    """View function for displaying event certificates."""
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('This event is not yours')
    if request.method == 'GET':
        # Calculate remaining certificates to be generated
        qtd_certificados = evento.participantes.all().count() - Certificado.objects.filter(evento=evento).count()
        return render(request, 'certificados_evento.html', {'evento': evento, 'qtd_certificados': qtd_certificados})

def gerar_certificado(request, id):
    """View function for generating certificates for event participants."""
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('This event is not yours')

    # Paths for template and font files
    path_template = os.path.join(settings.BASE_DIR, 'templates/static/evento/img/template_certificado.png')
    path_fonte = os.path.join(settings.BASE_DIR, 'templates/static/fontes/arimo.ttf')

    for participante in evento.participantes.all():
        # TODO: Validate if certificate already exists for this participant and event
        
        # Load certificate template image
        img = Image.open(path_template)
        draw = ImageDraw.Draw(img)

        # Load fonts and add text to certificate
        fonte_nome = ImageFont.truetype(path_fonte, 60)
        fonte_info = ImageFont.truetype(path_fonte, 30)
        draw.text((230, 651), f"{participante.username}", font=fonte_nome, fill=(0, 0, 0))
        draw.text((761, 782), f"{evento.nome}", font=fonte_info, fill=(0, 0, 0))
        draw.text((816, 849), f"{evento.carga_horario} hours", font=fonte_info, fill=(0, 0, 0))

        # Save generated certificate to in-memory file
        output = BytesIO()
        img.save(output, format="PNG", quality=100)
        output.seek(0)
        img_final = InMemoryUploadedFile(output,
                                         'ImageField',
                                         f'{token_urlsafe(8)}.png',
                                         'image/jpeg',
                                         sys.getsizeof(output),
                                         None)

        # Create Certificado object and save to database
        certificado_gerado = Certificado(
            certificado=img_final,
            participantes=participante,
            evento=evento,
        )
        certificado_gerado.save()

    messages.add_message(request, constants.SUCCESS, 'Certificates generated')
    return redirect('certificados_evento', kwargs={'id': evento.id})

def procurar_certificado(request, id):
    """View function for searching a certificate by email."""
    evento = get_object_or_404(Evento, id=id)
    if not evento.criador == request.user:
        raise Http404('This event is not yours')

    email = request.POST.get('email')
    certificado = Certificado.objects.filter(evento=evento).filter(participantes__email=email).first()

    if not certificado:
        messages.add_message(request, constants.ERROR, 'Certificate not found')
        return redirect(reverse('certificados_evento', kwargs={'id': evento.id}))

    return redirect(certificado.certificado.url)
