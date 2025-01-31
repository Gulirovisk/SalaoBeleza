from django.contrib import admin
from .models import *

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'telefone_whatsapp')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissional', 'horario_inicio', 'horario_fim')

@admin.register(Galeria)
class GaleiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem')
