from django.shortcuts import redirect, render
from app_tvshow.models import show

# Create your views here.
def index(request):
    context = {
      "all_shows": show.objects.all(), 
    }
    return render(request, 'index.html', context)

def view(request, id):
    context = {
        "show": show.objects.get(id = id)
    }
    return render(request, "view.html", context)

def new_form(request):
    
    return render(request, 'create.html')

def new(request):
    print(request.POST)

    show.objects.create(title = request.POST['title'], \
        network = request.POST['network'], \
        releaseDate = request.POST['releaseDate'], \
        desc = request.POST['desc'])
    id = show.objects.get(title = request.POST['title'], \
        network = request.POST['network'], \
        releaseDate = request.POST['releaseDate']).id
    return redirect(f'/shows/{id}')

def update(request, id):
    show2update = show.objects.get(id = id)
    show2update.title = request.POST['title']
    show2update.network = request.POST['network']
    show2update.releaseDate = request.POST['releaseDate']
    show2update.desc = request.POST['desc']
    show2update.save()
    return redirect(f'/shows/{id}')

def edit(request, id):
    context = {
        "show": show.objects.get(id = id)
    }
    return render(request, "edit.html", context)

def delete(request, id):
    show_to_delete = show.objects.get(id=id)	
    show_to_delete.delete()	
    return redirect('/shows')