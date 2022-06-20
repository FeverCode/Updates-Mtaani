from django.views import View
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView

# Create your views here.
def dispatch(self, request, *args, **kwargs):
       # will redirect to the home page if a user tries to access the register page while logged in
       if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
       return super(RegisterView, self).dispatch(request, *args, **kwargs)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect('login')

        return render(request, self.template_name, {'form': form})
    

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class IndexView(ListView):
    model = Neighbourhood
    template_name = 'index.html'
    context_object_name = 'hoods'


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            # prevents post get redirect pattern. sends a get request instead of post request
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'users/profile.html', context)


@login_required
def user_profile(request):
    profile = Profile.objects.all()
    posts = Post.objects.all().order_by('id').reverse()
    return render(request, 'users/users-profile.html', {'profile': profile, 'posts': posts})


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'photo','post','neighbourhood']
    template_name = 'create_post.html'
    success_url = 'post.html'
    #   ↓        ↓ method of the CreatePostView
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #   ↓              ↓ method of the CreatePostView
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Create new post'
        return data
@login_required
def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})

@login_required
def business(request):
    business = Business.objects.all()
    return render(request, 'business.html', {'business': business})

@login_required
def contacts(request):
    contacts = Neighbourhood.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})
