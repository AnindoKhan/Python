from django.shortcuts import render, redirect
def index (request):
    return render(request, "index.html")
def result(request):
    print("did it work?")
    your_name = request.POST["name"]
    dojo_location = request.POST["dojo_location"]
    favorite_language=request.POST["python"]
    comment=request.POST["comment"]

    context={
        "one": your_name,
        "two": dojo_location,
        "three": favorite_language,
        "four": comment,
    }

    

    return render (request,"index.html",context)
