from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Rango says hello world! <a href = '/rango/about'> About</a>")

def about(request):
	return HttpResponse('Django says here is your about page')