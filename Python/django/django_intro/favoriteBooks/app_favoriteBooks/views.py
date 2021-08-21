from django.shortcuts import render, redirect
from django.contrib import messages
from app_favoriteBooks.models import User, UserManager, Book, BookManager
import bcrypt

# Create your views here.


def index(request):
    request.session.flush()
    return render(request, 'index.html')


def register(request):  # post redirect
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # hash the password
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        # create a user
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST[
                'last_name'], email=request.POST['email'], password=hashed_pw
        )
        # create a session
        request.session['user_id'] = new_user.id
        return redirect('/books')
    return redirect('/')


# render the success page


def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0], 
        'all_books': Book.objects.all()
    }

    return render(request, 'books.html', context)

def add_book(request):
    print(request.POST)
    errors = Book.objects.reg_validator(request.POST)
    this_user = User.objects.filter(id=request.POST['uploaded_by'])

    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        request.session['user_id'] = this_user[0].id
        return redirect('/books')
    else:
        Book.objects.create(title = request.POST['title'], \
            description = request.POST['description'], \
            uploaded_by = User.objects.get(id=request.POST['uploaded_by']))
        Book.objects.last().users_who_like.add(User.objects.get(id=request.POST['uploaded_by'])) 
        return redirect('/books')

def user_book(request, user_id, book_id):
    request.session['user_id'] = user_id
    print("I was here")
    return redirect('/books/{}'.format(book_id))

def book(request, book_id):
    this_user = User.objects.get(id=request.session['user_id'])
    context ={
        'this_user': this_user,
        'book': Book.objects.get(id = book_id),
        'uploaded_by': Book.objects.get(id = book_id).uploaded_by,
        'users_who_like': Book.objects.get(id = book_id).users_who_like.all()
    }
    print(context)
    return render(request, 'book.html', context)

def add_favorite(request, user_id, book_id):
    Book.objects.get(id = book_id).users_who_like.add(User.objects.get(id=user_id)) 
    request.session['user_id'] = user_id
    return redirect('/books/{}'.format(book_id))

def update_description(request):
    print("I'm here")
    book_id = int(request.POST['book_id'])
    book_to_update = Book.objects.get(id = book_id)
    book_to_update.description = request.POST['description']
    book_to_update.save()
    return redirect('/books/{}'.format(book_id))

def delete_book(request):
    book_id = int(request.POST['book_id'])
    book_to_update = Book.objects.get(id = book_id)
    book_to_update.delete()
    return redirect('/books')
# log in

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/books')
    return redirect('/')
# log out


def logout(request):
    request.session.flush()
    return redirect('/')