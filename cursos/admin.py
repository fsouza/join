from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import *

class CursoAdmin(ModelAdmin):
    list_display = ('titulo', 'carga_horaria',)
    search_fields = ('titulo', 'descricao',)
    list_filter = ('instrutor',)

class InstrutorAdmin(ModelAdmin):
     list_display = ('nome',)
     search_fields = ('nome',)

admin.site.register(Aluno)
admin.site.register(Instrutor)
admin.site.register(Inscricao)
admin.site.register(Telefone)
admin.site.register(Curso)
admin.site.register(Material)
