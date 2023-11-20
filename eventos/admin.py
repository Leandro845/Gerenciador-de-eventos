from django.contrib import admin
from .models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'data_inicio',
        'data_termino',
        'carga_horario'
    )
    list_filter = (
        'id',
        'nome',
        'data_inicio',
        'data_termino',
        'carga_horario'
    )


admin.site.register(Evento, EventoAdmin)
