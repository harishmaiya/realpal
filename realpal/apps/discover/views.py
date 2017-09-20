from django.shortcuts import render
from django.views import View


class DiscoverView(View):
    template_name = 'discover/discover.html'

    def get(self, request, *args, **kwargs):
        url_name = request.GET.get('url_name', '')
        return render(request, self.template_name, context={'url_name': url_name}, status=200)
