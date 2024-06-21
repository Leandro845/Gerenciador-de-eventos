from django.urls import path
from . import views

urlpatterns = [
    # Define a path for '/meus_certificados/' URL
    path('meus_certificados/', views.meus_certificados, name='meus_certificados')
]
