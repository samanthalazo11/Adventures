from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Destination(models.Model):
    location = models.CharField(max_length=100)
    budget = models.IntegerField(default=0)
    dates= models.CharField(max_length=100)
    flights = models.CharField(max_length=100)
    hotel= models.CharField(max_length=100)
    notes = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location
    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs ={'destination_id':self.id})

class Restauraunts(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} Description: {self.description}"

class Excursions(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price =  models.IntegerField(default=0)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} is {self.price}"
