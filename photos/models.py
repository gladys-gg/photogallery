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
        
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
        
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
        
    def get_category_id(cls,id):
        category = Category.object.get(pk = id)
        return category

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
        
class Photo(models.Model):
    title = models.CharField(max_length =50)
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    description = models.TextField(max_length =100)
    image = models.ImageField(upload_to = 'photos/', default='No image')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

    def save_photo(self):
        self.save()
        
    def delete_photo(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def get_all_photos(cls):
        all_photos = Photo.objects.all()
        return all_photos
    
    @classmethod
    def get_photo_by_id(cls, id):
        a_photo = Photo.objects.get(id=id)
        return a_photo    