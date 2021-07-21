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
class BookManager(models.Manager):
    def book_validate (self,postData):
        errors = {}
        if len(postData['title']) == 0:
            errors['title_length'] ="Title is required"
        if len(postData['description']) < 5:
            errors['description_length'] = "Description must be atleast 5 charaters"
        return errors
class Book (models.Model):
    title = models.CharField(max_length = 255)
    descrption = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name= "books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = "liked_books")
    updated_at = models.DateTimeField(auto_now_add =True)
    created_at = models.DateTimeField(auto_now_add =True)
    objects = BookManager()

# Create your models here.

