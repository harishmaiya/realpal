from django import forms
from realpal.apps.users.models import User


class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'zipcode', 'phone_number', 'email']
