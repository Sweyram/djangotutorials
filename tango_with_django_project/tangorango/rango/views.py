from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am from the context"}
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	return HttpResponse('Django says here is your about page')