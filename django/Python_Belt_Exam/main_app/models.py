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
        
        # user = User.email.fitler (email=postData["email"]):
        # if len(user)> 0:
        #     errors['emails_taken'] = "Email is already taken"

class User (models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email= models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)
    objects = UserManager()

class TripManager(models.Manager):
    def trip_validate(self,postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors['destination_length'] = "Destination is atleast 3 characters"
        if postData['destination'].isalpha() == False:
            errors['destination_char'] = "Destination cannot contain special characters"
        if len(postData['start_date']) == 0:
            errors['start_date'] = "Start Date is required"
        if len(postData['end_date']) == 0:
            errors['end_date'] = "End Date is required"
        if len(postData['plan']) == 0:
            errors['plan'] = "Plan is required"
        return errors 
        

class Trip (models.Model):
    destination = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    trip_creator = models.ForeignKey(User, related_name= "trips_made",on_delete = models.CASCADE)
    travelers = models.ManyToManyField(User, related_name = "trips_joined")
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)
    objects = TripManager()

