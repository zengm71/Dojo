from django.shortcuts import redirect, render, HttpResponse
from time import gmtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string


# Create your views here.
def display(request):

    print('here in function display')
    print(request.session['result'])
    context = {
        'string': request.session['result']['string'],
        'counter': request.session['result']['counter']
    }
    print(context)
    return render(request, 'index.html', context)

def init(request):
    
    request.session.flush()
    request.session['result'] = {
        'string': get_random_string(length=14),
        'counter': 1
    }
    print('here in function init')

    return redirect('/random_word')

def generate(request):
    if request.method == 'GET':
        print('redirecting')
        return redirect('/')
    print('here in function generate')
    print(request.session['result'])
    request.session['result']['string'] = get_random_string(length=14)
    request.session['result']['counter'] += 1
    request.session.modified = True
    print(request.session['result'])
    return redirect('/random_word')
    # context = {
    #     'string': request.session['result']['string'],
    #     'counter': request.session['result']['counter']
    # }
    # print(context)
    # return render(request, 'index.html', context)

def reset(request):
    if request.method == 'GET':
        print('redirecting')
        return redirect('/')
    print('here in function reset')
    request.session['result']['string'] = get_random_string(length=14)
    request.session['result']['counter'] = 0
    request.session.modified = True

    print(request.session['result'])
    return redirect('/random_word')

    # context = {
    #     'string': request.session['result']['string'],
    #     'counter': request.session['result']['counter']
    # }
    # print(context)
    # return render(request, 'index.html', context)