from django.conf.urls.defaults import *

urlpatterns = patterns('cursos.views',
            url(r'^$', 'cursos'),
            url(r'^(?P<slug>[\w_-]+)/$', 'curso'),
            url(r'^instrutores/(?P<slug>[\w_-]+)$', 'instrutor'),
)
