from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = (
        'id',               # Display the event's ID
        'nome',             # Display the event's name
        'data_inicio',      # Display the event's start date
        'data_termino',     # Display the event's end date
        'carga_horario'     # Display the event's duration
    )

    # Add filters for the admin list view
    list_filter = (
        'id',               # Filter by event's ID
        'nome',             # Filter by event's name
        'data_inicio',      # Filter by event's start date
        'data_termino',     # Filter by event's end date
        'carga_horario'     # Filter by event's duration
    )

# Register the Evento model with its admin configuration
admin.site.register(Evento, EventoAdmin)
