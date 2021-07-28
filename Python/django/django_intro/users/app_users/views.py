from django.shortcuts import redirect, render
from app_users.models import Users

# Create your views here.
def index(request):
    context = {
    	"all_users": Users.objects.all()
    }
    return render(request, 'index.html', context)

def addUser(request):
    print(request.POST)
    Users.objects.create(first_name = request.POST['first_name'], \
        last_name = request.POST['first_name'], \
        email_address = request.POST['email'], \
        age = request.POST['age'])
    return redirect('/')