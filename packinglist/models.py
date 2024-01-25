from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='trips')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='items')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name