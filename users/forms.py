from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # this is a required field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] # this is the order in which the fields will appear on the form

