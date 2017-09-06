from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View

from realpal.apps.onboarding.forms import PurchaseStepForm, MaritalStatusForm, FirstHomeForm, HouseTypeForm, \
    CityForm, MaxBudgetForm, CurrentRentForm, HowSoonForm, PersonalProfileForm
from realpal.apps.users.models import User, City, PasswordReset
from django.utils.decorators import method_decorator

from .mixins import anonymous_required


@method_decorator(anonymous_required, name='dispatch')
class PurchaseStepView(View):

    template_name = 'onboarding/purchase_step.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'purchase_step': request.session.get('purchase_step', None)}
        form = PurchaseStepForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'purchase_step': request.session.get('purchase_step', None)}
        form = PurchaseStepForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['purchase_step'] = form.cleaned_data['purchase_step']
            return HttpResponseRedirect(reverse('onboarding:marital-status'))
        return render(request, self.template_name, {'form': form}, status=400)


@method_decorator(anonymous_required, name='dispatch')
class MaritalStatusView(View):

    template_name = 'onboarding/marital_status.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'marital_status': request.session.get('marital_status', None)}
        form = MaritalStatusForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'marital_status': request.session.get('marital_status', None)}
        form = MaritalStatusForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['marital_status'] = form.cleaned_data['status']
            return HttpResponseRedirect(reverse('onboarding:first-home'))
        return render(request, self.template_name, {'form': form}, status=400)


@method_decorator(anonymous_required, name='dispatch')
class FirstHomeView(View):

    template_name = 'onboarding/first_home.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'first_home': request.session.get('first_home', None)}
        form = FirstHomeForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'first_home': request.session.get('first_home', None)}
        form = FirstHomeForm(request.POST or None, initial=registration_data)
        if form.is_valid():
            request.session['first_home'] = form.cleaned_data['firsthome']
            return HttpResponseRedirect(reverse('onboarding:house-type'))
        return render(request, self.template_name, {'form': form}, status=400)


@method_decorator(anonymous_required, name='dispatch')
class HouseTypeView(View):

    template_name = 'onboarding/house_type.html'

    def get(self, request, *args, **kwargs):
        registration_data = {
            'house_type': request.session.get('house_type', ''),
            'house_age': request.session.get('house_age', ''),
            'house_condition': request.session.get('house_condition', '')
        }
        house_type_form = HouseTypeForm(initial=registration_data)

        return render(
            request,
            self.template_name,
            {
                'house_type_form': house_type_form,

            },
            status=200
        )

    def post(self, request, *args, **kwargs):
        registration_data = {
            'house_type': request.session.get('house_type', ''),
            'house_age': request.session.get('house_age', ''),
            'house_condition': request.session.get('house_condition', '')
        }
        house_type_form = HouseTypeForm(request.POST or None, initial=registration_data)

        if house_type_form.is_valid():
            request.session['house_type'] = house_type_form.cleaned_data['house_type']
            request.session['house_age'] = house_type_form.cleaned_data['house_age']
            request.session['house_condition'] = house_type_form.cleaned_data['house_cond']
            return HttpResponseRedirect(reverse('onboarding:city'))

        return render(
            request,
            self.template_name,
            {
                'house_type_form': house_type_form,
            }, status=400
        )


@method_decorator(anonymous_required, name='dispatch')
class CityView(View):

    template_name = 'onboarding/city.html'

    def get(self, request, *args, **kwargs):
        form = CityForm()
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)
        if form.data['preferred_city']:
            request.session['city'] = form.data['preferred_city']
        return HttpResponseRedirect(reverse('onboarding:max-budget'))


@method_decorator(anonymous_required, name='dispatch')
class MaxBudgetView(View):

    template_name = 'onboarding/max_budget.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'max_budget': request.session.get('max_budget', '')}
        form = MaxBudgetForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'max_budget': request.session.get('max_budget', '')}
        form = MaxBudgetForm(request.POST or '', initial=registration_data)
        if form.is_valid():
            request.session['max_budget'] = form.cleaned_data['budget']
            return HttpResponseRedirect(reverse('onboarding:current-rent'))
        return render(request, self.template_name, {'form': form}, status=400)


@method_decorator(anonymous_required, name='dispatch')
class CurrentRentView(View):

    template_name = 'onboarding/current_rent.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'current_rent': request.session.get('current_rent', '')}
        form = CurrentRentForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'current_rent': request.session.get('current_rent', '')}
        form = CurrentRentForm(request.POST or '', initial=registration_data)
        if form.is_valid():
            request.session['current_rent'] = form.cleaned_data['current_rent']
            return HttpResponseRedirect(reverse('onboarding:how-soon'))
        return render(request, self.template_name, {'form': form}, status=400)


@method_decorator(anonymous_required, name='dispatch')
class HowSoonView(View):

    template_name = 'onboarding/how_soon.html'

    def get(self, request, *args, **kwargs):
        registration_data = {'how_soon': request.session.get('how_soon', '')}
        form = HowSoonForm(initial=registration_data)
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        registration_data = {'how_soon': request.session.get('how_soon', '')}
        form = HowSoonForm(request.POST or '', initial=registration_data)
        if form.is_valid():
            request.session['how_soon'] = form.cleaned_data['how_soon']
            return HttpResponseRedirect(reverse('onboarding:personal-profile'))
        return render(request, self.template_name, {'form': form}, status=400)


@method_decorator(anonymous_required, name='dispatch')
class PersonalProfileView(View):

    template_name = 'onboarding/personal_profile.html'

    def get(self, request, *args, **kwargs):
        form = PersonalProfileForm()
        return render(request, self.template_name, {'form': form}, status=200)

    def post(self, request, *args, **kwargs):
        form = PersonalProfileForm(request.POST or None)
        if form.is_valid():
            try:
                city = City.objects.get(id=request.session.get('city', ''))
            except (ValueError, City.DoesNotExist):
                city = None
            user = User.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                zipcode=form.cleaned_data['zipcode'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                username=form.cleaned_data['email'],

                purchase_step=request.session.get('purchase_step', None),
                status=request.session.get('marital_status', None),
                firsthome=request.session.get('first_home', None),
                house_type=request.session.get('house_type', None),
                house_age=request.session.get('house_age', None),
                house_cond=request.session.get('house_condition', None),
                preferred_city=city,
                budget=request.session.get('max_budget', None),
                current_rent=request.session.get('current_rent', None),
                how_soon=request.session.get('how_soon', None),

                is_active=False

            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            user.send_confirmation_email()

            return render(
                request,
                'onboarding/onboarding_complete.html',
                {
                    'success': 'Congratulations, you have completed the onboarding process successfully',
                    'user': user,
                },
                status=302
            )
        return render(request, self.template_name, {'form': form}, status=400)


class ResendActivationEmail(View):
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id', '')
        try:
            user = User.objects.get(id=user_id)
            user.send_confirmation_email()
        except(User.DoesNotExist, ValueError):
            pass
        return render(
            request,
            'onboarding/onboarding_complete.html',
            {
                'success': 'Your Activation Email has been resent',
                'user': user,
            },
            status=302
        )


class ActivateAccount(View):
    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid', '')
        instance = PasswordReset.objects.filter(uuid=uuid)
        if not instance.count() == 1:
            return HttpResponseRedirect('onboarding:activation-error')
        user = instance[:1].get().user
        user.is_active = True
        user.save()
        instance.delete()
        user.send_welcome_email()
        return render(
            request,
            'onboarding/activation_success.html',
            {
                'success': 'Congratulations, you have registered successfully'
            },
            status=200
        )
