from django import forms
from django.contrib.auth.forms import UserCreationForm

from realpal.apps.users import User


class PurchaseStepForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['purchase_step']
        widgets = {'purchase_step': forms.RadioSelect}


class MaritalStatusForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['status']
        widgets = {'status': forms.RadioSelect}


class FirstHomeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firsthome']


class HouseTypeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['house_type', 'house_age', 'house_cond']
        widgets = {
            'house_type': forms.RadioSelect,
            'house_age': forms.RadioSelect,
            'house_cond': forms.RadioSelect
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['preferred_city']
        widgets = {'preferred_city': forms.Select}


class MaxBudgetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['budget']


class CurrentRentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['current_rent']


class HowSoonForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['how_soon']


class PersonalProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'zipcode', 'phone_number', 'email']
