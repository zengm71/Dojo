from django.shortcuts import render, redirect
from django.contrib import messages
from app_login.models import Users
import bcrypt
# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    print(request.POST)
    errors = Users.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    elif len(Users.objects.filter(email = request.POST['email'])) > 0:
        messages.error(request, 'User email already exists')
        return redirect('/')
    else:
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(request.POST['password'].encode(), salt).decode()
        password_cf = bcrypt.hashpw(request.POST['password_cf'].encode(), salt).decode()
        Users.objects.create(first_name = request.POST['first_name'], \
            last_name = request.POST['last_name'], \
            email = request.POST['email'], \
            password = password, \
            password_cf = password_cf)
        context = {
            'form': 'register',
            'first_name': request.POST['first_name']
        }
    return render(request, 'success.html', context)

def login(request):
    if len(Users.objects.filter(email = request.POST['email'])) > 0:
        user = Users.objects.get(email = request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            context = {
                'form': 'login',
                'first_name': user.first_name
            }
            return render(request, 'success.html', context)
        else:
            context = {
                'form': 'login',
                'error': 'password is wrong'
            }
            return render(request, 'index.html', context)
    else:
        context = {
            'form': 'login',
            'error': 'no such email'
        }
        return render(request, 'index.html', context)
