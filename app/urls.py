from django.urls import path, include
from app import views
from .views import RegisterView
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .forms import LoginForm
from django.conf.urls import url


urlpatterns = [
    path('',views.index, name='index'),
    path('register/',RegisterView.as_view(), name='users-register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user/profile/', views.user_profile, name='users-profile'),
    path('post/create/', views.CreatePostView.as_view(), name='new-post'),
    path('post/save/', views.post, name='post'),
    path('business/', views.business, name='business'),
    path('contacts/', views.contacts, name='contacts'),
   
]
