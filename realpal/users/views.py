from django.shortcuts import HttpResponse, reverse, get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User

from realpal.apps.registration.forms import PurchaseStepForm, MaritalStatusForm, FirstHomeForm, HouseTypeForm, \
    HouseAgeForm, HouseConditionForm, CityForm, MaxBudgetForm, CurrentRentForm, HowSoonForm, PersonalProfileForm


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
        'marital_status_form': MaritalStatusForm,
        'first_home_form': FirstHomeForm,
        'house_type_form': HouseTypeForm,
        'house_age_form': HouseAgeForm,
        'House_condition_form': HouseConditionForm,
        'city_form': CityForm,
        'max_budget_form': MaxBudgetForm,
        'current_rent_form': CurrentRentForm,
        'how_soon_form': HowSoonForm,
        'personal_profile_form': PersonalProfileForm,
    }

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        for form in self.forms:
            context[form] = self.forms[form]
        return context

    def get_object(self):
        return self.request.user

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        for form in self.forms:
            if form in request.POST:
                form_class = self.get_form_class()
                form_name = form
                break

        form = self.get_form(form_class)

        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})

    def get_success_url(self):
        return HttpResponse('Profile Updated successfully')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
