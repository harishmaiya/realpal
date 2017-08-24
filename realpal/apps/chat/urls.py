from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import ChatRoomView

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'chat/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'},  name='logout'),
    url(r'^room/$', ChatRoomView.as_view(), name='chat-room'),

]
