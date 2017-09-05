from django.conf.urls import url

from realpal.apps.chat.views import ChatRoomView
from realpal.apps.chat.api import MessageCreateAPIView

urlpatterns = [
    url(r'^$', ChatRoomView.as_view(), name='chat-room'),
    url(r'^(?P<room_id>[0-9]+)/', ChatRoomView.as_view(), name='chat-room'),
    url(r'^file/$', MessageCreateAPIView.as_view(), name='chat-file'),

]
