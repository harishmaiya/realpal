from django import forms
from realpal.users.models import User, City


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
        widgets = {'firsthome': forms.RadioSelect}


class HouseTypeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['house_type']
        widgets = {'house_type': forms.RadioSelect}


class HouseAgeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['house_age']
        widgets = {'house_age': forms.RadioSelect}


class HouseConditionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['house_cond']
        widgets = {'house_cond': forms.RadioSelect}


class CityForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget={forms.RadioSelect})


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
        fields = ['current_rent']
