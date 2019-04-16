from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout 
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, ProfileForm
from .models import Profile

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')

    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user) # User의 Profile 생성
            auth_login(request, user)
            return redirect('posts:list')
        
    else:
        signup_form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people':people})
    
def update(request):
    user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {'user_change_form':user_change_form})
    

def profile_update(request):
    profile = request.user.profile
    if request.method = "POST":
        profile_form = ProfileForm(request  instance=profile)
    return render(request, 'accounts/profile_update.html', {
                                                            'profile_form':profile_form,
                                                            })