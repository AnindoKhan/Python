from django.db import models
    
class Dojo(models.Model):
    name= models.CharField(max_length=255)
    city = models.CharField(max_length =255)
    state = models.CharField(max_length=2)
    desc = models.TextField()


class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name = "ninjas", on_delete = models.CASCADE)
    name= models.CharField(max_length=255)
    city = models.CharField(max_length =255)
    state = models.CharField(max_length=2)
    

