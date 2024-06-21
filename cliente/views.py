from django.shortcuts import render
from eventos.models import Certificado  # Import Certificado model from eventos app models


def meus_certificados(request):
    # Query Certificado objects where the current user is a participant
    certificados = Certificado.objects.filter(participantes=request.user)
    
    # Render the meus_certificados.html template with certificados context
    return render(request, 'meus_certificados.html', {'certificados': certificados})
