from cmath import e
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

#Create a UserUpdateForm to update the user's profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta: 
        model = User
        fields = ['username', 'email']
        
#Create a ProfileUpdateForm to update the user's profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','neighbourhood' ,'location', 'p_photo', 'bio']

