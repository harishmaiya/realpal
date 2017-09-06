from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View


@method_decorator(login_required, name='get')
class DiscoverView(View):
    template_name = 'discover/discover.html'

    def get(self, request, *args, **kwargs):
        context = {
            'display_text': 'Discover View'
        }

        return render(request, self.template_name, context=context, status=200)
