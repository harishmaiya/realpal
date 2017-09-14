from django.shortcuts import render
from django.views import View


class DiscoverView(View):
    template_name = 'discover/discover.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={}, status=200)
