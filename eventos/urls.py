from django.urls import path
from . import views  # Importing views from the current app

# URL patterns for app 'evento'
urlpatterns = [
    path('novo_evento/', views.novo_evento, name='novo_evento'),  # Route for creating a new event
    path('gerenciar_evento/', views.gerenciar_evento, name='gerenciar_evento'),  # Route for managing events
    path('inscrever_evento/<int:id>/', views.inscrever_evento, name='inscrever_evento'),  # Route for registering for an event
    path('inscricao_realizada/', views.inscricao_realizada, name='inscricao_realizada'),  # Route for showing registration success
    path('participantes_evento/<int:id>/', views.participantes_evento, name='participantes_evento'),  # Route for displaying event participants
    path('gerar_csv/<int:id>/', views.gerar_csv, name='gerar_csv'),  # Route for generating CSV of event participants
    path('certificados_evento/<int:id>/', views.certificados_evento, name='certificados_evento'),  # Route for displaying event certificates
    path('gerar_certificado/<int:id>/', views.gerar_certificado, name='gerar_certificado'),  # Route for generating certificates for event participants
    path('procurar_certificado/<int:id>/', views.procurar_certificado, name='procurar_certificado'),  # Route for searching certificate by email
]
