from django.shortcuts import render 
from time import gmtime, strftime
from datetime import datetime

def index (request):
    context= {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render (request,'index.html', context)

# Create your views here.

