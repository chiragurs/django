from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")#Httpresponse(HTML statement as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to home page</h1>")

def html_demo1(request):
    return render(request,"sample.html")