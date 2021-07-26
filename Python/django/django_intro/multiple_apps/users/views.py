# Create your views here.
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all users")

def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

