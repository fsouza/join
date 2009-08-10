#coding:utf-8
# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Instrutor, Curso
from forms import AlunoForm

def cursos(request):
    cursos = Curso.objects.all()
    return render_to_response('cursos.html', locals(), context_instance = RequestContext(request))

def cadastro(request):
    form = AlunoForm()
    return render_to_response('cadastro_aluno.html', locals(), context_instance = RequestContext(request))

def cadastrar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Cadastro efetuado com sucesso!'

        return render_to_response('cadastro_aluno.html', locals(), context_instance = RequestContext(request))
    else:
        return HttpResponse('Esta página deve tratar um formulário, não acesse-a diretamente.')

@login_required
def instrutor(request, slug):
    instrutor = get_object_or_404(Instrutor, slug = slug)
    return render_to_response('instrutor.html', locals(), context_instance = RequestContext(request))

@login_required
def curso(request, slug):
    curso = get_object_or_404(Curso, slug = slug)
    return render_to_response('curso.html', locals(), context_instance = RequestContext(request))

@login_required
def inscricao(request, slug):
    curso = get_object_or_404(Curso, slug = slug)
    return render_to_response('inscricao.html', locals(), context_instance = RequestContext(request))

