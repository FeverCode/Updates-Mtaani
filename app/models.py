import email
from email.policy import default
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
     admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mtaani')
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
         return self.name
     
     class Meta:
        ordering = ['name']
         

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    location = models.CharField(max_length=25, default='Nairobi')
    p_photo = CloudinaryField('image', default='https://res.cloudinary.com/fevercode/image/upload/v1654534329/default_n0r7rf.png')
    bio = models.TextField(max_length=255, default='This is your bio', blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    

        
        
class Business(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood , on_delete=models.CASCADE, related_name='businesses')
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
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    photo = CloudinaryField('image', default='https://res.cloudinary.com/fevercode/image/upload/v1655640806/tim-mossholder-H6eaxcGNQbU-unsplash_aq5n8o.jpg')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='mtaani_post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} Post'
        
    def create_post(self):
        self.save()
    
    
