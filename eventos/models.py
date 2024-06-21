from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # ForeignKey to User who created the event
    nome = models.CharField(max_length=200)  # Event name, max length 200 characters
    descricao = models.TextField()  # Event description as text
    data_inicio = models.DateField()  # Event start date
    data_termino = models.DateField()  # Event end date
    carga_horario = models.IntegerField()  # Event duration in hours
    logo = models.FileField(upload_to='logos')  # Event logo uploaded to 'logos/' directory
    participantes = models.ManyToManyField(User, related_name='evento_participantes')  # Many-to-Many relationship with User model for participants

    # Color palette
    cor_principal = models.CharField(max_length=7)  # Primary color of the event
    cor_secundaria = models.CharField(max_length=7)  # Secondary color of the event
    cor_fundo = models.CharField(max_length=7)  # Background color of the event

    def __str__(self):
        return self.nome  # String representation of the Evento instance returns its name

class Certificado(models.Model):
    certificado = models.ImageField(upload_to='certificados')  # Certificate image uploaded to 'certificados/' directory
    participantes = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # ForeignKey to User who received the certificate
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)  # ForeignKey to Evento related to the certificate

