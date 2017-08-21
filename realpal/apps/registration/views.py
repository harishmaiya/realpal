from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.views import View

from realpal.apps.registration.forms import PurchaseStepForm, MaritalStatusForm, FirstHomeForm, HouseTypeForm, \
    HouseAgeForm, \
    HouseConditionForm, CityForm, MaxBudgetForm, CurrentRentForm, HowSoonForm, PersonalProfileForm
from realpal.users.models import User


class PurchaseStepView(View):

    template_name = 'registration/purchase_step.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'purchase_step': request.session.get('purchase_step', None)}
        form = PurchaseStepForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'purchase_step': request.session.get('purchase_step', None)}
        form = PurchaseStepForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['purchase_step'] = form.cleaned_data['purchase_step']
            return HttpResponseRedirect(reverse('register:marital-status'))
        return render(request, self.template_name, {'form': form}, status=400)


class MaritalStatusView(View):

    template_name = 'registration/marital_status.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'marital_status': request.session.get('marital_status', None)}
        form = MaritalStatusForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'marital_status': request.session.get('marital_status', None)}
        form = MaritalStatusForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['marital_status'] = form.cleaned_data['status']
            return HttpResponseRedirect(reverse('register:first-home'))
        return render(request, self.template_name, {'form': form}, status=400)


class FirstHomeView(View):

    template_name = 'registration/first_home.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'first_home': request.session.get('first_home', None)}
        form = FirstHomeForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'first_home': request.session.get('first_home', None)}
        form = FirstHomeForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['first_home'] = form.cleaned_data['firsthome']
            return HttpResponseRedirect(reverse('register:house-type'))
        return render(request, self.template_name, {'form': form}, status=400)


class HouseTypeView(View):

    template_name = 'registration/house_type.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'house_type': request.session.get('house_type', None)}
        house_type_form = HouseTypeForm(initial=registration_data)

        registration_data = {'house_age': request.session.get('house_age', None)}
        house_age_form = HouseAgeForm(initial=registration_data)

        registration_data = {'house_condition': request.session.get('house_condition', None)}
        house_condition_form = HouseConditionForm(initial=registration_data)

        return render(
            request,
            self.template_name,
            {
                'house_type_form': house_type_form,
                'house_age_form': house_age_form,
                'house_condition_form': house_condition_form
            },
            status=200
        )

    def post(self, request, *args, **kwargs):
        registration_data = {'house_type': request.session.get('house_type', None)}
        house_type_form = HouseTypeForm(request.POST or None, initial=registration_data)

        registration_data = {'house_age': request.session.get('house_age', None)}
        house_age_form = HouseAgeForm(request.POST or None, initial=registration_data)

        registration_data = {'house_condition': request.session.get('house_condition', None)}
        house_condition_form = HouseConditionForm(request.POST or None, initial=registration_data)

        if house_type_form.is_valid() and house_age_form.is_valid() and house_condition_form.is_valid():
            request.session['house_type'] = house_type_form.cleaned_data['house_type']
            request.session['house_age'] = house_age_form.cleaned_data['house_age']
            request.session['house_condition'] = house_condition_form.cleaned_data['house_cond']
            return HttpResponseRedirect(reverse('register:city'))

        return render(
            request,
            self.template_name,
            {
                'house_type_form': house_type_form,
                'house_age_form': house_age_form,
                'house_condition_form': house_condition_form
            }, status=400
        )


class CityView(View):

    template_name = 'registration/city.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'city': request.session.get('city', None)}
        form = CityForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'city': request.session.get('city', None)}
        form = CityForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['city'] = form.cleaned_data['city']
            return HttpResponseRedirect(reverse('register:max-budget'))
        return render(request, self.template_name, {'form': form}, status=400)


class MaxBudgetView(View):

    template_name = 'registration/max_budget.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'max_budget': request.session.get('max_budget', None)}
        form = MaxBudgetForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'max_budget': request.session.get('max_budget', None)}
        form = MaxBudgetForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['max_budget'] = form.cleaned_data['budget']
            return HttpResponseRedirect(reverse('register:current-rent'))
        return render(request, self.template_name, {'form': form}, status=400)


class CurrentRentView(View):

    template_name = 'registration/current_rent.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'current_rent': request.session.get('current_rent', None)}
        form = CurrentRentForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'current_rent': request.session.get('current_rent', None)}
        form = CurrentRentForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['current_rent'] = form.cleaned_data['current_rent']
            return HttpResponseRedirect(reverse('register:how-soon'))
        return render(request, self.template_name, {'form': form}, status=400)


class HowSoonView(View):

    template_name = 'registration/how_soon.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'how_soon': request.session.get('how_soon', None)}
        form = HowSoonForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'how_soon': request.session.get('how_soon', None)}
        form = HowSoonForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['how_soon'] = form.cleaned_data['how_soon']
            return HttpResponseRedirect(reverse('register:personal-profile'))
        return render(request, self.template_name, {'form': form}, status=400)


class PersonalProfileView(View):

    template_name = 'registration/personal_profile.html'

    def get(self, request, *args, **kwargs):
        form = PersonalProfileForm()
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        form = PersonalProfileForm(request.POST or None)
        if form.is_valid():
            user = User.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                zipcode=form.cleaned_data['zipcode'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],

                purchase_step=request.session.get('purchase_step', None),
                status=request.session.get('marital_status', None),
                firsthome=request.session.get('first_home', None),
                house_type=request.session.get('house_type', None),
                house_age=request.session.get('house_age', None),
                house_cond=request.session.get('house_condition', None),
                budget=request.session.get('max_budget', None),
                current_rent=request.session.get('current_rent', None),
                how_soon=request.session.get('how_soon', None),

            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return HttpResponse('Well Done on finishing registration', status=302)
        return render(request, self.template_name, {'form': form}, status=400)
