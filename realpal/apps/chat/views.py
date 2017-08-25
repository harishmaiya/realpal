from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View

from realpal.apps.chat.models import Room, Message
from realpal.apps.users.constants import CLIENT_USER


@method_decorator(login_required, name='get')
class ChatRoomView(View):
    template_name = 'chat/room.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == CLIENT_USER:
            room = Room.objects.get(client=user)
            messages = Message.objects.filter(room=room)
            context = {
                'messages': messages,
                'selected_client_room': room.id
            }
        else:
            selected_client_room = self.kwargs.get('room_id')
            messages = Message.objects.filter(room_id=selected_client_room) if selected_client_room else []
            client_rooms = Room.objects.all()
            my_clients = [client_room for client_room in client_rooms if client_room.agent == user]
            unassigned_clients = [client_room for client_room in client_rooms if client_room.agent is None]
            context = {
                'my_clients': my_clients,
                'unassigned_clients': unassigned_clients,
                'agent_user': True,
                'selected_client_room': selected_client_room if selected_client_room else None,
                'messages': messages
            }

        return render(request, self.template_name, context=context, status=200)
