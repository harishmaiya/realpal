from django.shortcuts import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.forms.models import model_to_dict

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User

from realpal.apps.registration.forms import PurchaseStepForm, MaritalStatusForm, FirstHomeForm, HouseTypeForm, \
    CityForm, MaxBudgetForm, CurrentRentForm, HowSoonForm, PersonalProfileForm


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = PurchaseStepForm  # this will be the default form that is submitted by default
    success_url = '/users/edit'
    forms = {
        'purchase_step_form': PurchaseStepForm,
        'marital_status_form': MaritalStatusForm,
        'first_home_form': FirstHomeForm,
        'house_type_form': HouseTypeForm,
        'city_form': CityForm,
        'max_budget_form': MaxBudgetForm,
        'current_rent_form': CurrentRentForm,
        'how_soon_form': HowSoonForm,
        'personal_profile_form': PersonalProfileForm,
    }

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        forms = {
            'purchase_step_form': PurchaseStepForm(initial=model_to_dict(self.get_object())),
            'marital_status_form': MaritalStatusForm(initial=model_to_dict(self.get_object())),
            'first_home_form': FirstHomeForm(initial=model_to_dict(self.get_object())),
            'house_type_form': HouseTypeForm(initial=model_to_dict(self.get_object())),
            'city_form': CityForm(initial=model_to_dict(self.get_object())),
            'max_budget_form': MaxBudgetForm(initial=model_to_dict(self.get_object())),
            'current_rent_form': CurrentRentForm(initial=model_to_dict(self.get_object())),
            'how_soon_form': HowSoonForm(initial=model_to_dict(self.get_object())),
            'personal_profile_form': PersonalProfileForm(initial=model_to_dict(self.get_object())),
        }
        context.update(forms)
        return context

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, *args, **kwargs):
        for form in self.forms:
            if form in request.POST:
                self.form_class = self.forms[form]
                break
        return super(UserUpdateView, self).post(self, request, *args, **kwargs)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
