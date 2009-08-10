from django.shortcuts import render_to_response
from django.template import RequestContext

def bemvindo(request):
    return render_to_response('bemvindo.html', locals(), context_instance = RequestContext(request))
