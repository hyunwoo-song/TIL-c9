from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= get_user_model
        fields = UserCreationForm.Meta.fields
        
class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model =


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'introduction', 'image']
        