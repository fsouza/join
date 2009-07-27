from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Instrutor(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.TextField()
    slug = models.SlugField(max_length = 100, blank = True, unique = True)

    def get_url(self):
        return reverse('cursos.views.instrutor', kwargs = { 'slug' : self.slug })

    def __unicode__(self):
        return self.nome

class Curso(models.Model):
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

class Material(models.Model):
    arquivo = models.FileField(upload_to = 'cursos/materiais')
    curso = models.ForeignKey('Curso')

class Aluno(User):
    cpf = models.CharField(max_length = 11)

    def __unicode__(self):
        return self.username

class Telefone(models.Model):
    ddd = models.CharField(max_length = 2)
    numero = models.CharField(max_length = 8)
    proprietario = models.ForeignKey('Aluno')

    def __unicode__(self):
        return '(%s) %s' % (self.ddd, self.numero)

class Inscricao(models.Model):
    status = models.BooleanField()
    aluno = models.ForeignKey('Aluno')
    curso = models.ForeignKey('Curso')
