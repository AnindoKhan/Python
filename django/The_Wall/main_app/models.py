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
class Message (models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User, related_name='messages',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Comment (models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)