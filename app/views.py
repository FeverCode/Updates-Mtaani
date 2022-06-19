from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request, 'index.html', {'hoods': hoods})


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
    success_url = 'post'

    #   ↓        ↓ method of the CreatePostView
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    #   ↓              ↓ method of the CreatePostView
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Create new post'
        return data

def post(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})


def business(request):
    business = Business.objects.all()
    return render(request, 'business.html', {'business': business})
