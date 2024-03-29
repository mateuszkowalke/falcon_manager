from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """Form definition for ProfileUpdate."""

    class Meta:
        """Meta definition for ProfileUpdateform."""

        model = Profile
        fields = ['img', 'city', 'zip_code', 'street', 'house_number', 'vet_number']
