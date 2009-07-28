from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import Aluno, Instrutor, Inscricao, Telefone, Curso, Material

class CursoAdmin(ModelAdmin):
    list_display = ('titulo', 'carga_horaria',)
    search_fields = ('titulo', 'descricao',)
    list_filter = ('instrutor',)

class InstrutorAdmin(ModelAdmin):
     list_display = ('nome',)
     search_fields = ('nome',)

admin.site.register(Aluno)
admin.site.register(Instrutor, InstrutorAdmin)
admin.site.register(Inscricao)
admin.site.register(Telefone)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Material)
