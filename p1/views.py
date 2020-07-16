from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")#Httpresponse(HTML statement as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to home page</h1>")