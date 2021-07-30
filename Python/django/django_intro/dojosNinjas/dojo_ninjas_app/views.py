from django.shortcuts import redirect, render
from dojo_ninjas_app.models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
    	"all_dojos": Dojo.objects.all(), 
        "all_ninjas": Ninja.objects.all()

    }
    return render(request, 'index.html', context)

def addDojo(request):
    print(request.POST)
    Dojo.objects.create(name = request.POST['name'], \
        city = request.POST['city'], \
        state = request.POST['state'], \
        desc = 'nothing')
    return redirect('/')

def addNinja(request):
    print(request.POST)
    Ninja.objects.create(first_name = request.POST['first_name'], \
        last_name = request.POST['last_name'], \
        dojo = Dojo.objects.filter(name = request.POST['dojo'])[0])
    return redirect('/')