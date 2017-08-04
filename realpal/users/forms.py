from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    zipcode = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=15)

    ## User Profile Fields
    status = forms.CharField(max_length=5)
    firsthome = forms.CharField(max_length=5)
    home_type = forms.CharField(max_length=5)
    howsoon = forms.CharField(max_length=5)
    max_budget = forms.CharField(max_length=50)
    rent = forms.CharField(max_length=50)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.zipcode = self.cleaned_data['zipcode']
        user.phone = self.cleaned_data['phone']

        user.status = self.cleaned_data['status']

        firsthome = self.cleaned_data['firsthome']

        if firsthome == 'N':
            user.firsthome = False
        else:
            user.firsthome = True

        user.home_type = self.cleaned_data['home_type']
        user.howsoon = self.cleaned_data['howsoon']
        user.budget = float(self.cleaned_data['max_budget'])
        user.current_rent = float(self.cleaned_data['rent'])

        user.save()
