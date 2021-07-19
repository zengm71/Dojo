from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("placeholder to later display a list of all blogs")
    return render(request, "index.html")

def create(request):
    return HttpResponse("placeholder to later display a new form to create a new blog")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return HttpResponse(f"placeholder to delete blog {number}")

def hello_name(request, name):
    context = {
        "htmlname": name,
        "nameslist": ['A', "B", "c", "D"]

    }
    return render(request, "helloname.html", context)