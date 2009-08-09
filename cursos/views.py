# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Instrutor, Curso

def instrutor(request, slug):
    instrutor = get_object_or_404(Instrutor, slug = slug)
    return render_to_response('instrutor.html', locals(), context_instance = RequestContext(request))

def curso(request, slug):
    curso = get_object_or_404(Curso, slug = slug)
    return render_to_response('curso.html', locals(), context_instance = RequestContext(request))

def cursos(request):
    cursos = Curso.objects.all()
    return render_to_response('cursos.html', locals(), context_instance = RequestContext(request))

def inscricao(request, slug):
    curso = get_object_or_404(Curso, slug = slug)
    return render_to_response('inscricao.html', locals(), context_instance = RequestContext(request))
