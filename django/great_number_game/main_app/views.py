from django.shortcuts import render, HttpResponse, redirect
import random 
def index(request):
    if 'random_num' in request.session:
        pass
    else:
        request.session['random_num']= random.randint(1,100)
    return render (request,"index.html")

def guess(request):
    random_num = request.session['random_num']
    print(random_num),
    new_num = request.POST['user_num']
    if random_num > int(new_num):
        return render(request, "low.html")
    
    if random_num < int(new_num):
        return render(request, "high.html")
    
    if random_num == int(new_num):
        request.session.clear()
        return render (request, "correct.html")

