from django.shortcuts import redirect, render
from books_authors_app.models import Book, Author

def index(request):
    context = {
        "all_books": Book.objects.all(), 
        "all_authors": Author.objects.all()
    }
    return render(request, 'books.html', context)

def authors(request):
    context = {
        "all_books": Book.objects.all(), 
        "all_authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)

def addBook(request):
    print(request.POST)
    Book.objects.create(title = request.POST['title'], \
        desc = request.POST['desc'])
    return redirect('/')

def addAuthor(request):
    print(request.POST)
    Author.objects.create(first_name = request.POST['first_name'], \
        last_name = request.POST['last_name'], \
        notes = request.POST['notes'])
    return redirect('/authors')

def book(request, book_id):
    print(book_id)
    context = {
        "book": Book.objects.get(id=book_id), 
        "all_authors": Author.objects.all()
    }
    return render(request, 'book.html', context)

def addAuthor2Book(request, book_id):
    fn = request.POST['authorName'].split(" ")[0]
    ln = request.POST['authorName'].split(" ")[1]
  
    Book.objects.get(id=book_id).authors.\
        add(Author.objects.get(first_name = fn, \
            last_name = ln))
    
    return redirect(f'/books/{book_id}')

def author(request, author_id):
    print(author_id)
    context = {
        "author": Author.objects.get(id=author_id), 
        "all_books": Book.objects.all()
    }
    return render(request, 'author.html', context)

def addBook2Author(request, author_id):
  
    Author.objects.get(id=author_id).books.\
        add(Book.objects.get(title = request.POST['bookTitle']))
    
    return redirect(f'/authors/{author_id}')