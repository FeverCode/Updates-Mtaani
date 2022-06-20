from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.db.models import Q

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
    success_url = reverse_lazy ('post')
    
    
    #   ↓        ↓ method of the CreatePostView
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #   ↓              ↓ method of the CreatePostView
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Create new post'
        return data
    
    
class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'mtaani_post'
    
    

class BusinessView(LoginRequiredMixin, ListView):
    model = Business
    template_name = 'business.html'
    context_object_name = 'business'


@login_required
def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('joined-hood')


def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('joined-hood')


class JoinedHoodView(LoginRequiredMixin, ListView):
    model = Neighbourhood
    template_name = 'joined_hood.html'


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "business": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
