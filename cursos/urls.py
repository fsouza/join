from django.conf.urls.defaults import *

urlpatterns = patterns('cursos.views',
            url(r'^$', 'cursos'),
            url(r'^(?P<slug>[\w_-]+)/$', 'curso'),
            url(r'^instrutores/(?P<slug>[\w_-]+)$', 'instrutor'),
            url(r'^inscricao/(?P<slug>[\w_-]+)$', 'inscricao'),
            url(r'^alunos/cadastro/$', 'cadastro'),
            url(r'^alunos/cadastrar/$', 'cadastrar'),
)
