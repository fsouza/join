from django.db import models

# Create your models here.
class Instrutor(models.Model):
    nome = models.CharField(max_length = 100)

class Curso(models.Model):
    titulo = models.CharField(max_length = 300)
    carga_horaria = models.IntegerField()
    instrutor = models.ForeignKey(Instrutor)
