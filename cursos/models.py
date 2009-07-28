#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from util.signals import curso_pre_save, instrutor_pre_save
from django.db.models import signals
from django.utils.translation import gettext_lazy

# Create your models here.
class Instrutor(models.Model):
    class Meta:
        ordering = ('nome',)
        verbose_name = gettext_lazy('Instrutor')
        verbose_name_plural = gettext_lazy('Instrutores')

    nome = models.CharField(max_length = 200)
    descricao = models.TextField()
    slug = models.SlugField(max_length = 100, blank = True, unique = True)

    def get_url(self):
        return reverse('cursos.views.instrutor', kwargs = { 'slug' : self.slug })

    def __unicode__(self):
        return self.nome

class Curso(models.Model):
    class Meta:
        ordering = ('titulo',)
        verbose_name = gettext_lazy('Curso')
        verbose_name_plural = gettext_lazy('Cursos')

    titulo = models.CharField(max_length = 300)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    instrutor = models.ForeignKey('Instrutor')
    pre_requisitos = models.TextField()
    slug = models.SlugField(max_length = 100, blank = True, unique = True)

    def get_url(self):
        return reverse('cursos.views.curso', kwargs = { 'slug' : self.slug })

    def __unicode__(self):
        return self.titulo

class Aluno(User):
    class Meta:
        ordering = ('first_name', 'username',)
        verbose_name = gettext_lazy('Aluno')
        verbose_name_plural = gettext_lazy('Alunos')

    cpf = models.CharField(max_length = 11)

    def __unicode__(self):
        return self.username

class Telefone(models.Model):
    class Meta:
        verbose_name = gettext_lazy('Telefone')
        verbose_name_plural = gettext_lazy('Telefones')

    ddd = models.CharField(max_length = 2)
    numero = models.CharField(max_length = 8)
    proprietario = models.ForeignKey('Aluno')

    def __unicode__(self):
        return '(%s) %s' % (self.ddd, self.numero)

class Inscricao(models.Model):
    class Meta:
        verbose_name = gettext_lazy('Inscrição')
        verbose_name_plural = gettext_lazy('Inscrições')


    status = models.BooleanField()
    aluno = models.ForeignKey('Aluno')
    curso = models.ForeignKey('Curso')

# Conectando sinais
signals.pre_save.connect(instrutor_pre_save, sender = Instrutor)
signals.pre_save.connect(curso_pre_save, sender = Curso)
