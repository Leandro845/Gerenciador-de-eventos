from django.urls import path  # Import the path function from django.urls
from . import views  # Import the views module from the current package

# Define the URL patterns for the application
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),  # URL pattern for the registration view
    path('login/', views.login, name='login')  # URL pattern for the login view
]
