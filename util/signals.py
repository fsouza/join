#coding:utf-8
from django.db.models import signals
from django.template.defaultfilters import slugify
from cursos.models import Instrutor
from cursos.models import Curso

def instrutor_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nome)
        novo_slug = slug
        contador = 0

        while Instrutor.objects.filter(slug = novo_slug).exclude(id = instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d' % (slug, contador)

        instance.slug = novo_slug

def curso_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        novo_slug = slug
        contador = 0

        while Curso.objects.filter(slug = novo_slug).exclude(id = instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d' % (slug, contador)

        instance.slug = novo_slug

# Conectando sinais
signals.pre_save.connect(instrutor_pre_save, sender = Instrutor)
signals.pre_save.connect(curso_pre_save, sender = Curso)
