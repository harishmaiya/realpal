from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import ChatRoomView

urlpatterns = [
    url(r'^room/$', ChatRoomView.as_view(), name='chat-room'),
    url(r'^room/(?P<room_id>[0-9]+)/', ChatRoomView.as_view(), name='chat-room'),
]
