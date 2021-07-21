from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
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
    return redirect ("/home")
def home(request):
    user = User.objects.get (id = request.session['user_id'])
    users_meals = Meal.objects.filter(date = date.today())
    print(users_meals)
    today_goal = Goal.objects.filter(start_date = date.today())
    print (today_goal)
    user_exercises = Exercise.objects.filter(date= date.today())
    burned_caolories=0
    calorie_count = 0
    protein_count = 0
    carbohydrates_count = 0
    fat_count = 0 
    for burned in user_exercises:
        if user == burned.exercise_finisher:
            burned_caolories += burned.calories_burned
    for meal in users_meals:
        if meal.meal_eater == user:
            calorie_count += meal.calories 
            protein_count += meal.protein
            carbohydrates_count += meal.carbohydrates
            fat_count += meal.fat
    context ={
        "user": user,
        'today_date_calorie':calorie_count,
        "today_date_protein": protein_count,
        "today_date_carbohydrates": carbohydrates_count,
        "today_date_fat": fat_count,
        "today_date_burned": burned_caolories,
        "today_goal":today_goal
    }
    return render (request, "home.html", context)
def login (request):
    existing_user =User.objects.filter(email = request.POST['email'])
    print(existing_user)
    if len(existing_user) > 0:
        user = existing_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
                # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
            return redirect ('/home')
        else:
            messages.error(request, "Email or Password does not match, try again")
            return redirect ('/')
    else:
        messages.error(request,"EMAIL DOES NOT EXIST")
        return redirect ('/')
def logout(request):
    request.session.flush()
    return redirect ('/')
def newExercise(request):
    return render (request, "exercise.html")
def addExercise(request):
    exercise = Exercise.objects.create(
        activity = request.POST['activity'],
        duration = request.POST['duration'],
        calories_burned = request.POST['calories_burned'],
        date= request.POST['date'],
        exercise_finisher = User.objects.get (id = request.session['user_id'])
    )
    return redirect ('/exercises')
def editExercise(request, exercise_id):
    current_exercise = Exercise.objects.get(id=exercise_id)
    context ={
        'exercise': current_exercise
    }
    return render (request, "edit_exercise.html", context)
def updateExercise(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise.activity = request.POST['activity']
    exercise.calories_burned = request.POST['calories_burned']
    exercise.date = request.POST['date']
    exercise.duration = request.POST['duration']
    exercise.save()
    return redirect('/exercises')
def exerciseDelete(request, exercise_id):
    current_exercise = Exercise.objects.get(id=exercise_id)
    current_exercise.delete()
    return redirect('/exercises')
def newMeal(request):
    return render(request, "add_meal.html")
def addMeal(request):
    new_meal = Meal.objects.create(
        calories = request.POST['calories'],
        meal = request.POST['meal'],
        protein = request.POST['protein'],
        fat = request.POST['fat'],
        carbohydrates = request.POST['carbohydrates'],
        meal_eater =User.objects.get (id = request.session['user_id']),
        date = request.POST['date']
    )
    return redirect('/meals')
def updateMeal(request, meal_id):
    this_meal = Meal.objects.get(id=meal_id)
    context ={
        "meal": this_meal
    }
    return render (request,"edit_meal.html", context)
def editMeal(request, meal_id):
    edit_meal = Meal.objects.get(id=meal_id)
    edit_meal.meal = request.POST['meal']
    edit_meal.calories = request.POST['calories']
    edit_meal.protein = request.POST['protein']
    edit_meal.fat = request.POST['fat']
    edit_meal.carbohydrates = request.POST['carbohydrates']
    edit_meal.save()
    return redirect('/meals')
def deleteMeal(request, meal_id):
    this_meal = Meal.objects.get(id=meal_id)
    this_meal.delete()
    return redirect ('/meals')
def newGoal(request):
    return render (request, "add_goal.html")
def addGoal(request):
    new_goal = Goal.objects.create(
        description = request.POST['description'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        goal_setter = User.objects.get(id = request.session['user_id'])
    )
    return redirect  ('/goals')
def goalUpdate(request, goal_id):
    context ={
        "goal":Goal.objects.get(id=goal_id)
    }
    return render (request, "goal_update.html",context)
def goalEdit(request, goal_id):
    this_goal = Goal.objects.get(id=goal_id)
    this_goal.description = request.POST['description']
    this_goal.start_date = request.POST['start_date']
    this_goal.end_date = request.POST['end_date']
    this_goal.save()
    return redirect('/goals')
def goalDelete(request, goal_id):
    this_goal = Goal.objects.get(id = goal_id)
    this_goal.delete()
    return redirect ('/goals')
def meal(request):
    context ={
        "user":User.objects.get (id = request.session['user_id'])
    }
    return render (request,"meal.html",context)
def exercises(request):
    context ={
        "user":User.objects.get (id = request.session['user_id'])
    }
    return render (request,"your_exercises.html",context)
def goals(request):
    context ={
        "user":User.objects.get (id = request.session['user_id'])
    }
    return render (request,"goals.html",context)