from django.urls import path, include
from app import views


urlpatterns = [
    path('',views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('user/profile/', views.user_profile, name='users-profile'),
]
