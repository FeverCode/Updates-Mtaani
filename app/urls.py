from django.urls import path, include
from app import views
from .views import RegisterView


urlpatterns = [
    path('',views.index, name='index'),
    path('register/',RegisterView.as_view(), name='users-register'),
    path('profile/', views.profile, name='profile'),
    path('user/profile/', views.user_profile, name='users-profile'),
    path('post/create/', views.CreatePostView.as_view(), name='new-post'),
    path('post/save/', views.post, name='post'),
    path('business/', views.business, name='business'),
    path('contacts/', views.contacts, name='contacts'),
   
]
