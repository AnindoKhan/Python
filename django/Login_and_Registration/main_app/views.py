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
    return redirect ("/home")
def home(request):
    user = User.objects.get (id = request.session['user_id'])
    context ={
        "user": user
    }
    return render (request, "home.html", context)
def login (request):
    existing_user =User.objects.filter(email = request.POST['email'])
    print(existing_user)
    if len(existing_user) > 0:
        user = existing_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
            return redirect ('/home')
        else:
            messages.error(request, "Email or Password does not match, try again")
            return redirect ('/')
    else:
        messages.error(request,"EMAIL DOES NOT EXIST")
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect ('/')
