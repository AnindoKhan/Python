from django.db import models
class UserManager (models.Manager):
    def user_validate(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['first_name_length'] = "First Name is required"
        if postData['first_name'].isalpha() == False:
            errors['first_name_char'] = "First Name cannot contain special characters"
        if len(postData['last_name']) == 0:
            errors['last_name_length'] = "Last Name is required"
        if postData['last_name'].isalpha() == False:
            errors['last_name_char'] = "Last Name cannot contain special characters"
        if postData['password'] != postData['confirm_password']:
            errors ['passwords_match'] = "Password and Confirm must match"
        if len(postData['password']) < 8:
            errors['pasword_length'] = "Password must be atleast 8 characters"
        return errors

class User (models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email= models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)
    objects = UserManager()

class Exercise(models.Model):
    activity = models.TextField()
    duration = models.CharField(max_length= 255)
    calories_burned = models.IntegerField(null= True)
    date = models.DateField()
    exercise_finisher = models.ForeignKey(User, related_name = "exercises", on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)

class Goal(models.Model):
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    goal_setter = models.ForeignKey(User, related_name = "goals", on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)
class Meal(models.Model):
    calories = models.IntegerField(null= True)
    meal = models.CharField(max_length= 255)
    protein = models.IntegerField(null= True)
    carbohydrates = models.IntegerField(null= True)
    date = models.DateField()
    fat = models.IntegerField(null= True)
    meal_eater = models.ForeignKey(User,related_name = "meals", on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)


