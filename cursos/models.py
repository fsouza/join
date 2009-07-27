from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instrutor(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.TextField()
    slug = models.SlugField(max_length = 100, blank = True, unique = True)

class Curso(models.Model):
    titulo = models.CharField(max_length = 300)
    descricao = models.TextField()
    carga_horaria = models.IntegerField()
    instrutor = models.ForeignKey('Instrutor')
    pre_requisitos = models.TextField()
    slug = models.SlugField(max_length = 100, blank = True, unique = True)

class Material(models.Model):
    arquivo = models.FileField(upload_to = 'cursos/materiais')
    curso = models.ForeignKey('Curso')

class Aluno(User):
    cpf = models.CharField(max_length = 11)

class Telefone(models.Model):
    ddd = models.CharField(max_length = 2)
    numero = models.CharField(max_length = 8)
    proprietario = models.ForeignKey('Aluno')

class Inscricao(models.Model):
    status = models.BooleanField()
    aluno = models.ForeignKey('Aluno')
    curso = models.ForeignKey('Curso')
