from django import forms
from .models import Trip
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'participants']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']