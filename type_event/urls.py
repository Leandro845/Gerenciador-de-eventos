from django.contrib import admin  # Import the admin module
from django.urls import path, include  # Import path function and include function from django.urls
from django.conf.urls.static import static  # Import static function from django.conf.urls.static
from django.conf import settings  # Import settings from django.conf

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the Django admin site
    path('usuarios/', include('usuarios.urls')),  # URL pattern for the 'usuarios' app
    path('eventos/', include('eventos.urls')),  # URL pattern for the 'eventos' app
    path('cliente/', include('cliente.urls')),  # URL pattern for the 'cliente' app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

