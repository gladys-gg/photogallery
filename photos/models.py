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
        
class Category(models.Model):
    photo_category = models.CharField(max_length =30)

    def __str__(self):
        return self.photo_category
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()
        
class Poster(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name

    def save_poster(self):
        self.save()

        
    class Meta:
        ordering = ['first_name']
        
# class Image(models.Model):
#     title = models.CharField(max_length =50)
#     poster = models.ForeignKey(Poster)
#     description = models.TextField(max_length =100)
#     image = models.ImageField(upload_to = 'photos/', default='No image')
#     location = models.ForeignKey(Location)
#     category = models.ForeignKey(Category)
#     pub_date = models.DateTimeField(auto_now_add=True, null=True) 

#     def save_image(self):
#         self.save()
        
#     def delete_image(self):
#         self.delete()

#     def __str__(self):
#         return self.title