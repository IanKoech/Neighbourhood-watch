from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_pic= models.ImageField(upload_to='profile/' )
    bio = models.TextField(blank=True)
    more_info = models.TextField(blank=False, null=True)
    user = models.ForeignKey(User, null= True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bio
    
    def save_user(self):
        self.save()
