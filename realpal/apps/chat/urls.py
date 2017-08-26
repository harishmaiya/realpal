from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import ChatRoomView

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'},  name='logout'),
    url(r'^room/$', ChatRoomView.as_view(), name='chat-room'),
    url(r'^room/(?P<room_id>[0-9]+)/', ChatRoomView.as_view(), name='chat-room'),

]
