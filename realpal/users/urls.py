from django.conf.urls import url
from django.views.generic import TemplateView
from .models import User
from realpal.apps.registration.forms import PurchaseStepForm, MaritalStatusForm, FirstHomeForm, HouseTypeForm, \
    HouseAgeForm, HouseConditionForm, CityForm, MaxBudgetForm, CurrentRentForm, HowSoonForm, PersonalProfileForm
from .views import UserUpdateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name='home'),
    url(r'^messenger$', TemplateView.as_view(template_name='users/messenger.html'), name='messenger'),
    url(r'^edit$', view=UserUpdateView.as_view(), name='edit'),
]
