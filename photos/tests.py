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
        self.nature = Category(name='Nature')
        self.nature.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))
    
    def tearDown(self):
        self.nature.delete_category()


    def test_save_category(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
        
class ImageTest(TestCase):
    def setUp(self):
        self.Food = Category(name='Nature')
        self.Food.save_category()

        self.new_location = Location(name='Mombasa')
        self.new_location.save()

        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_image=Image(image_name='nature',image_description='nature')
        self.new_image.save_image() 

        self.new_image.Category.add(self.new_category)
        self.new_image.Location.add(self.new_location)
        self.new_image.Tags.add(self.new_tag)

        def tearDown(self):
            Image.objects.all().delete()
            Category.objects.all().delete()
            Location.objects.all().delete()
            Tags.objects.all().delete()

        def test_deleteImage(self):
            
            self.new_image.deleteImage()
            image = Image.objects.all()
            self.assertEqual(len(image),0 


        def test_get_all_photos(self):
            all_photos = Photo.get_all_photos()
            self.assertTrue(len(all_photos)>0)
        
        def test_get_photo_by_id(self):
            test_id=1
            a_photo = Image.objects.filter(test_id)
            self.assertTrue(len(a_photo)>0)


        def search_by_category(self):
            image = cls.objects.filter(category__name__icontains=search_term)
            return image
            self.assertTrue(len(search_term)==0)
    


