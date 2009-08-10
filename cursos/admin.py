try:
    import Image
except ImportError:
    from PIL import Image

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import Aluno, Instrutor, Inscricao, Telefone, Curso

class CursoAdmin(ModelAdmin):
    list_display = ('titulo', 'carga_horaria',)
    search_fields = ('titulo', 'descricao',)
    list_filter = ('instrutor',)

class InstrutorAdmin(ModelAdmin):
     list_display = ('nome',)
     search_fields = ('nome',)

     def save_model(self, request, obj, form, change):
         super(InstrutorAdmin, self).save_model(request, obj, form, change)
         if 'foto' in form.changed_data:
             extensao = obj.foto.name.split('.')[-1]

             nova_foto = Image.open(obj.foto.path)
             nova_foto.thumbnail((100, 100), Image.ANTIALIAS)

             obj.foto = 'cursos/fotos_instrutores/%d.%s' % (obj.id, extensao)
             nova_foto.save(obj.foto.path)
             obj.save()

admin.site.register(Aluno)
admin.site.register(Instrutor, InstrutorAdmin)
admin.site.register(Inscricao)
admin.site.register(Telefone)
admin.site.register(Curso, CursoAdmin)
