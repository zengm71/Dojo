from django.shortcuts import redirect, render
from django.contrib import messages
from app_courses.models import Course, Description, Comment

# Create your views here.
def index(request):
    context = {
        "all_courses": Course.objects.all(), 
        "all_desc": Description.objects.all()
    }
    return render(request, 'index.html', context)

def add(request):
    print(request.POST)
    errorsCourse = Course.objects.basic_validator(request.POST) 
    errorsDesc =  Description.objects.basic_validator(request.POST)

    errors = dict(list(errorsCourse.items())+list(errorsDesc.items()))
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/') 
    else:
        Course.objects.create(name = request.POST['name']) 
        Description.objects.create(desc = request.POST['desc'], \
            course = Course.objects.get(name = request.POST['name']))
    return redirect('/')

def destroy(request, id):
    context = {
        "course": Course.objects.get(id = id)
    }
    return render(request, "destroy.html", context)

def delete(delete, id):
    print(f"deleting {id}")
    courseToDelete = Course.objects.get(id = id)
    courseToDelete.delete()	
    return redirect('/')

def showComment(request, id):
    print(f"deleting {id}")
    context = {
        "course": Course.objects.get(id = id)
    }
    return render(request, "comments.html", context)

def addComment(request):
    id = request.POST['id']
    Comment.objects.create(comment = request.POST['comment'], course = Course.objects.get(id = id))
    return redirect(f'/courses/comment/{id}')