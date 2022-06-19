import email
from email.policy import default
from this import d
from django import http
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from cloudinary.models import CloudinaryField

# Create your models here.

class Neighbourhood(models.Model):
     name = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     occupants = models.IntegerField()
     admin = models.ForeignKey(User, on_delete=models.CASCADE)
     photo = CloudinaryField('image')
     description = models.TextField(max_length=255)
     hospital_tel = models.IntegerField(null=True, blank=True)
     police_tel = models.IntegerField(null=True, blank=True)
     
     
     def create_neighbourhood(self):
         self.save()
         
     def delete_neighbourhood(self):
            self.delete()
    
     def find_neighbourhood(neighbourhood_id):
         return Neighbourhood.objects.get(id=neighbourhood_id)
     
     def update_neighbourhood(self, new_neighbourhood):
         self.NeighbourhoodName = new_neighbourhood
         self.save()
    
     def update_occupants(self, new_occupants):
        self.OccupantsCount = new_occupants
        self.save()
        
     def __str__(self):
         return self.NeighbourhoodName
         

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    p_photo = CloudinaryField('image', default='https://res.cloudinary.com/fevercode/image/upload/v1654534329/default_n0r7rf.png')
    bio = models.TextField(max_length=255)
    def __str__(self):
        return f'{self.user.username} Profile'
        
        
class Business(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood , on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    
    def create_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
        
    def find_business(business_id):
        return Business.objects.get(id=business_id)
    
    def update_business(self, new_business):
        self.name = new_business
        self.save()
    
    def __str__(self):
        return self.name
    
    
    @classmethod 
    def search_business(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses
    
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
    def create_post(self):
        self.save()
    
    
