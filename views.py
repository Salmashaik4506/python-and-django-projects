from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req) :

    return render(req,('register.html'))


def add(req) :
    return HttpResponse("<h1> you mail is signed.. </h1>")
