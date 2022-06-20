from django.urls import path, include
from app import views
from .views import RegisterView
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, IndexView
from .forms import LoginForm
from django.conf.urls import url


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/',RegisterView.as_view(), name='users-register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),
    path('user/profile/', views.user_profile, name='users-profile'),
    path('post/create/', views.CreatePostView.as_view(), name='new-post'),
    path('post/save/', views.post, name='post'),
    path('business/', views.business, name='business'),
    path('contacts/', views.contacts, name='contacts'),
   
]
