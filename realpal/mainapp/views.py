from django.shortcuts import render
from django.views import View

from django.utils.decorators import method_decorator

from realpal.apps.onboarding.mixins import anonymous_required


@method_decorator(anonymous_required, name='dispatch')
class HomeView(View):

    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=200)
