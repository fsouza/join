from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os
dir = os.path.abspath(os.path.dirname(__file__))

urlpatterns = patterns('',
    # Example:
    # (r'^join/', include('join.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'views.bemvindo'),
    (r'^cursos/', include('cursos.urls')),
    (r'^media/(.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
    (r'^login/$', 'django.contrib.auth.views.login', { 'template_name' : 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', { 'template_name' : 'logout.html'}),
)
