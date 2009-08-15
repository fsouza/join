#coding:utf-8
from django.template.defaultfilters import slugify

def instrutor_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nome)
        new_slug = slug
        count = 0

        while sender.objects.filter(slug = new_slug).exclude(id = instance.id).count() > 0:
            count += 1
            new_slug = '%s-%d' % (slug, count)

        instance.slug = new_slug

def curso_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.titulo)
        new_slug = slug
        count = 0

        while sender.objects.filter(slug = new_slug).exclude(id = instance.id).count() > 0:
            count += 1
            new_slug = '%s-%d' % (slug, count)

        instance.slug = new_slug

def inscricao_post_save(signal, instance, sender, **kwargs):
    if instance.curso.vagas == instance.curso.inscricao_set.all().count() + 1:
        instance.curso.inscricoes_abertas = False
        instance.curso.save()
