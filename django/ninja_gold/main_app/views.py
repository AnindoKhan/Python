from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime
import random

def index(request):
    if 'total_gold' not in request.session:
        print("total gold = 0")
        request.session['total_gold']=0
        request.session['activities']=[]
    return render (request, "index.html")

def game (request):
    if request.POST['action']=='farm':
        number = random.randint(10,20)
        request.session['total_gold']+= number
        request.session['activities'].append(f'You entered the farm and earned {number} gold')
    elif request.POST['action']=='Cave':
        number = random.randint(5,10)
        request.session['total_gold']+= number
        request.session['activities'].append(f'You entered the cave and earned {number} gold')
    elif request.POST['action']=='House':
        number = random.randint(2,5)
        request.session['total_gold']+= number
        request.session['activities'].append(f'You entered the house and earned {number} gold')
    else:
        request.POST['action']=='casino'
        number = random.randint(-50,50)
        request.session['total_gold']+= number
        if number < 0:
            request.session['activities'].append(f'You entered the casino and lost {number} gold')
        else:
            request.session['activities'].append(f'You entered the casino and gained {number} gold')
    print(request.session['activities'])
    return redirect ('/')

def reset(request):
    request.session.clear()
    return redirect('/')
