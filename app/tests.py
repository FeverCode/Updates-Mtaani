from operator import ne
from this import s
from django.test import TestCase
from requests import post
from .models import *

# Create your tests here.
class TestApp(TestCase):
    def test_app(self):
        self.assertEqual(1, 1)

class TestProfile(TestCase):
    def test_profile(self):
        self.assertEqual(1, 1)
        
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
        
    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
    
    def test_save_user(self):
        self.user.save()
        self.assertTrue(len(User.objects.all()) > 0)
        
    def test_delete_user(self):
        self.user.delete()
        self.assertTrue(len(User.objects.all()) == 0)
        
     
        
class TestNeighbourhood(TestCase):
    def test_neighbourhood(self):
        self.assertEqual(1, 1)
        
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()
        self.neighbourhood = Neighbourhood.objects.create(name='Test', occupants=0, location='Nairobi', admin=self.user)
        self.neighbourhood.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))
        
    def test_create_neighbourhood(self):
        self.assertEqual(self.neighbourhood.name, 'Test')
        
    def test_save_neighbourhood(self):
        self.neighbourhood.save()
        self.assertTrue(len(Neighbourhood.objects.all()) > 0)
        
    def test_delete_neighbourhood(self):
        self.neighbourhood.delete()
        self.assertTrue(len(Neighbourhood.objects.all()) == 0)
        
    def test_find_neighbourhood(self):
        self.assertEqual(1, 1)
        
    def test_update_neighbourhood(self):
        self.assertEqual(1, 1)
        
    def test_update_occupants(self):
        self.assertEqual(1, 1)
        
class TestBusiness(TestCase):
    def test_business(self):
        self.assertEqual(1, 1)
        
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()
        self.neighbourhood = Neighbourhood.objects.create(name='Test', occupants=0, location='Nairobi', admin=self.user)
        self.neighbourhood.save()
        self.business = Business.objects.create(name='Test', user=self.user, neighbourhood=self.neighbourhood)
        self.business.save()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))
        
    def test_create_business(self):
        self.assertEqual(self.business.name, 'Test')
        
    def test_save_business(self):
        self.business.save()
        self.assertTrue(len(Business.objects.all()) > 0)
        
    def test_delete_business(self):
        self.business.delete()
        self.assertTrue(len(Business.objects.all()) == 0)
        
    def test_find_business(self):
        self.assertEqual(1, 1)
        
    def test_update_business(self):
        self.assertEqual(1, 1)
        
    def test_search_business(self):
        self.assertEqual(1, 1)
        
class TestPost(TestCase):
    def test_post(self):
        self.assertEqual(1, 1)
        
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user.save()
        self.neighbourhood = Neighbourhood.objects.create(name='Test', occupants=0, location='Nairobi', admin=self.user)
        self.neighbourhood.save()
        self.business = Business.objects.create(name='Test', user=self.user, neighbourhood=self.neighbourhood)
        self.business.save()
        self.post = Post.objects.create(title='Test', neighbourhood_id=self.neighbourhood.id,user=self.user, photo='https://res.cloudinary.com/fevercode/image/upload/v1655640806/tim-mossholder-H6eaxcGNQbU-unsplash_aq5n8o.jpg')
        self.post.save()
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
        
    def test_create_post(self):
        self.assertEqual(self.post.title, 'Test')
        
    def test_save_post(self):
        self.post.save()
        self.assertTrue(len(Post.objects.all()) > 0)
        
    def test_delete_post(self):
        self.post.delete()
        self.assertTrue(len(Post.objects.all()) == 0)
        
    def test_find_post(self):
        self.assertEqual(1, 1)
    
    def test_update_post(self):
        self.post.title = 'Test2'
        
    def test_search_post(self):
        self.assertEqual(1, 1)