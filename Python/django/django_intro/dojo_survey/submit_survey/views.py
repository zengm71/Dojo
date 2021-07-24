from django.shortcuts import redirect, render, HttpResponse, resolve_url

# Create your views here.
def index(request):
    print('got here from redirect!')
    return render(request, 'index.html')

def fillSurvey(request):
    print(request.method)
    if request.method == 'GET':
        print('redirecting')
        return redirect('/')
    
    request.session['result'] = {
        'name': request.POST['name'],
        'dojoLocation': request.POST['dojoLocation'],
        'favoriteLanguage': request.POST['favoriteLanguage'],
        'description': request.POST['description']
    }
    return redirect('/result')

def displaySurvey(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
