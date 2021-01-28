from django.db import models

# Create your models here.
class neighbourhood(models.Model):
    Name = models.CharField(max_length = 60)
    City = models.CharField(max_length = 30)
    Town = models.CharField(max_length = 60)
    Info = models.TextField(max_length=500)
    securitycontact = models.CharField(max_length=13)
    healthcontact = models.CharField(max_length=13)
    Occupantscount = models.IntegerField()
from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField

class Neighbourhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupantsCount = models.IntegerField(default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

 def __str__(self):
        return f'{self.user.username} Profile'
    def save_profile(self):
        self.save
    def delete_profile(self):
        self.delete()

class Business(models.Model):
    business_name = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email = models.CharField(max_length=30)
    