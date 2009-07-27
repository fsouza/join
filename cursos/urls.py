from django.conf.urls.defaults import *

urlpatterns = patterns('cursos.views',
            url(r'^$', 'cursos', name = 'cursos')
)
