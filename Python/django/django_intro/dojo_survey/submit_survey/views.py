from django.shortcuts import redirect, render, HttpResponse, resolve_url

# Create your views here.
def fillSurvey(request):
    if request.method == 'GET':
        print(request.GET)
        return render(request, 'index.html')
    if request.method == 'POST':
        return redirect("/result")

def displaySurvey(request):
    print(request.POST)
    context = {
        'name': request.POST['name'],
        'dojoLocation': request.POST['dojoLocation'],
        'favoriteLanguage': request.POST['favoriteLanguage'],
        'description': request.POST['description']
    }
    return render(request, "result.html", request.POST)