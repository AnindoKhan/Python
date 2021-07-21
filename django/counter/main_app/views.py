from django.shortcuts import render, redirect 

def index(request):
    request.session['counter'] += 1
    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    request.session['counter']=0
    return redirect('/')