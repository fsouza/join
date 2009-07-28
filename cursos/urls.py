from django.conf.urls.defaults import *

urlpatterns = patterns('cursos.views',
            url(r'^$', 'cursos'),
            url(r'^(?P<slug>[\w_-]+)/$', 'curso'),
)
