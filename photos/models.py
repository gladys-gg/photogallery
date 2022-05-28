from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    photo_location = models.CharField(max_length =30)

    def __str__(self):
        return self.photo_location
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()