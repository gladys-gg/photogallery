from django.test import TestCase
from .models import Poster,Location,Photo,Category
import datetime as dt

# Create your tests here.
class PosterTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.gaby= Poster(first_name = 'Gaby', last_name ='Mwangi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gaby,Poster))   
        
    # Testing Save Method
    def test_save_method(self):
        self.gaby.save_poster()
        posters = Poster.objects.all()
        self.assertTrue(len(posters) > 0) 
        
    def test_delete_method(self):
        self.gaby.save_poster()
        self.gaby.delete_poster()
        posters = Poster.objects.all()
        self.assertTrue(len(posters) == 0) 
        
    def test_display_method(self):
        self.gaby.save_poster()
        self.gaby.display_posters()
        poster = Poster.objects.all()
        self.assertTrue(len(posters) > 0) 
        
    def test_update_method(self):
        self.gaby.save_poster()
        new_poster = Poster.objects.filter(first_name="Gaby").update(first_name="Ryan")
        poster=Poster.objects.get(first_name="Ryan")
        self.assertTrue(posters.first_name,"Ryan")           

class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(location='Nairobi')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.nairobi.id)
        location.update_location('Mombasa')
        location = Location.get_location_id(self.nairobi.id)
        self.assertTrue(location.location == 'Mombasa')
    
    def tearDown(self):
        self.nairobi.delete_location() 
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.nature = Category(category='Nature')
        self.nature.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))
    
    def tearDown(self):
        self.nature.delete_category()
    


