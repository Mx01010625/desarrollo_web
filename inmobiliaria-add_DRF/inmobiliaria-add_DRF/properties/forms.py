from django.forms import ModelForm
from .models import Property
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = "__all__"

class SignupForm(UserCreationForm):
   class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)