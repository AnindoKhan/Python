from django.shortcuts import render, redirect
from .models import Dojo, Ninja
def index (request):
    all_dojos = Dojo.objects.all()
    context = {
        'all_dojos': all_dojos,
        'all_ninjas': Ninja.objects.all()
    }
    return  render (request, "index.html", context)

def dojo(request):
    #get info from post
    page_name = request.POST['name']
    page_city = request.POST['city']
    page_state = request.POST['state']

    #store in database
    Dojo.objects.create(
        name= page_name,
        city = page_city,
        state= page_state
    )
    return redirect ('/')
    #go back go mainpage

def ninja(request):
    name_ninja = request.POST['first_name'] + request.POST['last_name']
    The_Dojo = Dojo.objects.get(id= request.POST['dojo_id'])
    Ninja.objects.create(
        dojo = The_Dojo,
        name = name_ninja,
        city = "seattle",
        state = "WA"
    )
    return redirect ('/')