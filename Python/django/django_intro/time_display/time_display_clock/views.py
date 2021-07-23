from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from datetime import datetime


# Create your views here.
def default(request):
    return HttpResponse("Please go to localhost:8000/time for time display, thank you.")

def index(request):
    context = {
        # "date": strftime("%b-%d, %Y", gmtime()), 
        # "time":strftime("%H:%M %p", gmtime()),
        "date": datetime.now().strftime("%b-%d, %Y"), 
        "time": datetime.now().strftime("%H:%M %p")
    }
    return render(request,'index.html', context)


