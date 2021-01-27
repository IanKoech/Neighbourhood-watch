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

    def savehood(self):
        self.save()

    def deletehood(self):
        self.delete()

    def search(cls, searchterm):
        searchresults = cls.objects.filter(Name = searchterm)
        return searchresults
