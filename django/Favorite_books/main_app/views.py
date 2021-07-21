from django.shortcuts import render, redirect
from django.contrib import messages
from .models import * 
import bcrypt 
def index (request):
    return render (request, "index.html")

def register (request):
    errors = User.objects.user_validate(request.POST)
    print(errors)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect ('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
        )
    print (new_user.id)
    request.session['user_id'] = new_user.id
    return redirect ("/books")
def books(request):
    user = User.objects.get (id = request.session['user_id'])
    all_books = Book.objects.all().order_by("-created_at")
    context ={
        "user": user,
        "books": all_books
    }
    return render (request, "books.html", context)
def login (request):
    existing_user =User.objects.filter(email = request.POST['email'])
    print(existing_user)
    if len(existing_user) > 0:
        user = existing_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
            return redirect ('/books')
        else:
            messages.error(request, "Email or Password does not match, try again")
            return redirect ('/')
    else:
        messages.error(request,"EMAIL DOES NOT EXIST")
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect ('/')
def addBook(request):
    errors = Book.objects.book_validate(request.POST)
    print(errors)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect ('/books')
    else:
        book = Book.objects.create(
            title = request.POST['title'],
            descrption = request.POST['description'],
            uploaded_by = User.objects.get (id = request.session['user_id'])
        )
        book.users_who_like.add(User.objects.get (id = request.session['user_id']))
    return redirect ('/books')
def bookInfo(request, book_id):
    user = User.objects.get(id = request.session['user_id'])
    books = Book.objects.get(id=book_id)
    context ={
        "user": user,
        "books": books
    }
    return render (request,"book_info.html",context)
def edit (request, books_id):
        current_book = Book.objects.get(id = books_id)
        user = User.objects.get(id = request.session['user_id'])
        context ={
            "user": user,
            "books" : current_book
        }
        return render (request, "book_edit.html", context)
def editBook(request, books_id):
        errors = Book.objects.book_validate(request.POST)
        print(errors)
        if len(errors)> 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect (f"/books/{books_id}/edit")
        else:
            update_book = Book.objects.get (id = books_id)
            update_book.title = request.POST['title']
            update_book.descrption =request.POST['description']
            update_book.save()
            print(update_book)
        return redirect (f'/books/{books_id}')
def delete (request, books_id):
    book = Book.objects.get(id=books_id)
    book.delete()
    return render (request,"delete.html")

def favorite (request, books_id, user_id):
    book = Book.objects.get(id= books_id)
    user = User.objects.get(id = user_id)
    user.liked_books.add(book)
    return redirect (f'/books/{books_id}')

def unfavorite (request, books_id, user_id):
    book = Book.objects.get(id= books_id)
    user = User.objects.get(id = user_id)
    user.liked_books.remove(book)
    return redirect (f'/books/{books_id}')



