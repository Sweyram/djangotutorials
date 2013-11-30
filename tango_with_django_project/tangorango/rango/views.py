from django.http import HttpResponse
<<<<<<< HEAD
=======
from django.template import RequestContext
from django.shortcuts import render_to_response
>>>>>>> 6baa26752e8d40a0bd67c6fef3874401ffa360a6

# Create your views here.

def index(request):
<<<<<<< HEAD
	return HttpResponse("Rango says hello world! <a href = '/rango/about'> About</a>")
=======
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am from the context"}
	return render_to_response('rango/index.html', context_dict, context)
>>>>>>> 6baa26752e8d40a0bd67c6fef3874401ffa360a6

def about(request):
	return HttpResponse('Django says here is your about page')