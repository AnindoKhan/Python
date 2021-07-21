from django.shortcuts import render, redirect
from main_app.models import Book, Author
def index(request):
    context= {
        "books": Book.objects.all()
    }
    print(context["books"])

    return render (request, "index.html", context)

def create(request):
    title_post = request.POST['title']
    description_post = request.POST['description']
    Book.objects.create(
        title = title_post,
        desc = description_post
    )
    return redirect ('/')
def authors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render (request,"author.html", context)

def author_create(request):
    first_name_post =  request.POST['first_name']
    last_name_post =  request.POST['last_name']
    notes_post = request.POST['notes']
    Author.objects.create(
        first_name = first_name_post,
        last_name = last_name_post,
        notes = notes_post,
    )
    return redirect('/authors')
def show_book(request, book_id):
    book_from_db = Book.objects.get (id = book_id)
    context={
        "book" : book_from_db,
        "authors": book_from_db.authors.all(),
        "all_authors":Author.objects.all()

    }
    
    return render (request, "show_book.html",context)

def show_author(request, author_id):
    author_from_db = Author.objects.get (id = author_id)
    context={
        "author" : author_from_db,
        "books": author_from_db.books.all(),
        "all_books": Book.objects.all()
    }
    return render (request, "show_author.html",context)
def addBook(request):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author_id'])
    author.books.add(book)
    return redirect (f"/authors/{author.id}")

def addAuthor(request):
    id_book = int(request.POST['book_id'])
    id_author = int(request.POST['author_id'])
    my_book =Book.objects.get(id = id_book)
    my_author= Author.objects.get (id = id_author)
    my_book.authors.add(my_author)
    return redirect (f'/books/{id_book}')
    

# Create your views here.

