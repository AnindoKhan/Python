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
    return redirect ("/wall")
def wall(request):
    user = User.objects.get (id = request.session['user_id'])
    context ={
        "user": user,
        "messages":Message.objects.all().order_by("-created_at"),
    }
    return render (request, "wall.html", context)
def login (request):
    existing_user =User.objects.filter(email = request.POST['email'])
    print(existing_user)
    if len(existing_user) > 0:
        user = existing_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
            return redirect ('/wall')
        else:
            messages.error(request, "Email or Password does not match, try again")
            return redirect ('/')
    else:
        messages.error(request,"EMAIL DOES NOT EXIST")
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect ('/')
def message (request):
    if request.method == "GET":
        print ("this is a get method for the message")
        return render (request, "wall.html")
    if request.method == "POST":
        print ("message")
        Message.objects.create(
            message_text = request.POST['messages'],
            user = User.objects.get (id = request.session['user_id'])
            ) 
        return redirect('/wall')

def comment (request, message_id):
    if request.method == "GET":
        print ("this is a get method for the comment")
    if request.method == "POST":
        print ("comment")
        new_comment = Comment.objects.create(
            comment_text = request.POST['comment'],
            user = User.objects.get (id = request.session['user_id']),
            message = Message.objects.get (id = message_id)
            ) 
        return redirect('/wall')
def delete (request, message_id):
    delete_message = Message.objects.get(id=message_id)
    delete_message.delete()
    return redirect ("/wall")