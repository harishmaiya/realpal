from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View


@method_decorator(login_required, name='get')
class ChatRoomView(View):
    template_name = 'chat/room.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=200)
