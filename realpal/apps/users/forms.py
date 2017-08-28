from django import forms
from realpal.apps.users.models import User
from django.contrib.auth.forms import AuthenticationForm


class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'zipcode', 'phone_number', 'email']


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        label='Email address',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'id': ' email', 'class': 'input'})
    )
    password = forms.CharField(
        label='Password',
        max_length=255,
        required=True,
        widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'input'})
    )
