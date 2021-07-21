from django.shortcuts import render, redirect
from main_app.models import Show
from django.contrib import messages
def index(request):
    return redirect ("/shows")
def shows(request):
    context = {
        "shows" : Show.objects.all()
    }
    return render (request, "index.html", context)
def addShow(request):
    if request.method == "GET":
        return render (request,"addShow.html")
    
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len (errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/shows/new')
        else: 
            title_post = request.POST['title']
            network_post = request.POST['network']
            release_date_post = request.POST['release_date']
            description_post = request.POST['description']
            show = Show.objects.create(
                title = title_post,
                network = network_post,
                release_date =release_date_post,
                description = description_post,
            )
        return redirect (f"/shows/{show.id}")
def showInfo(request, show_id):
    context ={
        "shows" : Show.objects.get(id = show_id)
    }
    return render (request, "showInfo.html", context)
def edit(request, shows_id):
    if request.method =="GET":
        context ={
            "shows": Show.objects.get (id = shows_id)
        }
        return render (request, "edit.html",context)

    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len (errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f'/shows/{shows_id}/edit')
        else:
            shows = Show.objects.get(id = shows_id)
            shows.title = request.POST['title']
            shows.network = request.POST['network']
            shows.description = request.POST['description']
            shows.save()
        return redirect(f"/shows/{shows.id}")
def delete (request, shows_id):
    shows = Show.objects.get (id = shows_id)
    shows.delete()
    return redirect ('/') 
# Create your views here.
