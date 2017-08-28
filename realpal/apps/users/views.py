from django.shortcuts import reverse, render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, View
from django.forms.models import model_to_dict
from django.conf import settings
from .forms import LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User

from realpal.apps.registration.forms import PurchaseStepForm, MaritalStatusForm, FirstHomeForm, HouseTypeForm, \
    CityForm, MaxBudgetForm, CurrentRentForm, HowSoonForm
from realpal.apps.users.forms import PersonalProfileForm


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

    def get_success_url(self):
        return '{}{}'.format(reverse('users:update'), '#success')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/login.html', {'form': LoginForm})

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session.set_expiry(60 * 60 * 24)
                return redirect('dashboard')
            else:
                user.send_verification_email(user.email)
                return render(
                    request,
                    'home/login.html',
                    {
                        'form': LoginForm,
                        'error': 'You still have not verified your email address. The verification link has been '
                                 'resent to you email address'
                    },
                    status=401
                )
        else:
            return render(
                request,
                'users/login.html',
                {
                    'form': LoginForm,
                    'error': 'Make sure username and password are correct'
                },
                status=401
            )


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
