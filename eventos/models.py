from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    carga_horario = models.IntegerField()
    logo = models.FileField(upload_to='logos')
    participantes = models.ManyToManyField(User, related_name='evento_participantes')

    # Paleta de cores

    cor_principal = models.CharField(max_length=7)
    cor_secundaria = models.CharField(max_length=7)
    cor_fundo = models.CharField(max_length=7)

    def __str__(self):
        return self.nome


class Certificado(models.Model):
    certificado = models.ImageField(upload_to='certificados')
    participantes = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)

