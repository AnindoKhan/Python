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
    return redirect ("/dashboard")
def dashboard(request):
    user = User.objects.get (id = request.session['user_id'])
    trip = Trip.objects.all()
    context ={
        "user": user,
        "trips": trip,
    }
    return render (request, "dashboard.html", context)
def login (request):
    existing_user =User.objects.filter(email = request.POST['email'])
    print(existing_user)
    if len(existing_user) > 0:
        user = existing_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
            return redirect ('/dashboard')
        else:
            messages.error(request, "Email or Password does not match, try again")
            return redirect ('/')
    else:
        messages.error(request,"EMAIL DOES NOT EXIST")
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect ('/')
def create(request):
    user = User.objects.get (id = request.session['user_id'])
    context ={
        "user": user
    }
    return render (request, "new_trip.html",context)

def newTrip(request):
    errors = Trip.objects.trip_validate(request.POST)
    print(errors)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request,value)
            return redirect('/create')
    else:
        trip = Trip.objects.create(
            destination = request.POST['destination'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            plan = request.POST['plan'],
            trip_creator = User.objects.get (id = request.session['user_id'])
        )
        return redirect ('/dashboard')
def edit(request, trip_id):
    user = User.objects.get (id = request.session['user_id'])
    current_trip = Trip.objects.get(id = trip_id)
    context ={
        "trip": current_trip,
        "user":user
    }
    return render (request, "edit.html",context)
def update (request, trip_id):
    errors = Trip.objects.trip_validate(request.POST)
    print(errors)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request,value)
            return redirect(f'/edit/{trip_id}')
    else: 
        updated_trip = Trip.objects.get (id = trip_id)
        updated_trip.destination = request.POST['destination']
        updated_trip.start_date = request.POST['start_date']
        updated_trip.end_date = request.POST['end_date']
        updated_trip.plan = request.POST['plan']
        updated_trip.save()
        return redirect ('/dashboard')
def info(request, trip_id):
    user = User.objects.get (id = request.session['user_id'])
    trip = Trip.objects.get(id = trip_id)
    context ={  
        "trip":trip,
        "user":user
    }
    return render (request, "info.html", context)
def delete (request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.delete()
    return redirect ('/dashboard')