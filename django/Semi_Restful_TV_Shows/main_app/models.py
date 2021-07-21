from django.db import models
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "title should should be at least 1 character"
        if len (postData['network']) < 1:
            errors ["network"] = "network should be atleast 1 character"
        if len (postData['release_date']) < 1:
            errors ["release_date"] = "Release date should be atleast 1 character"
        if len(postData['description']) < 1:
            errors["description"] = "description should be at least 1 character"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.TextField()
    release_date = models.DateField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

