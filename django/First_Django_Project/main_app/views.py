from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
def root (request):
    return redirect ("/blogs")
def index(request):
    return HttpResponse("Place Holder to later display a list of blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")
def destroy(request, number):
    return redirect("/blogs")
def create(request):
    return redirect ("/")


# Create your views here.



