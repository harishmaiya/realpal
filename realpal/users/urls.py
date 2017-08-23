from django.conf.urls import url
from django.views.generic import TemplateView
from .views import UserUpdateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name='home'),
    url(r'^messenger$',TemplateView.as_view(template_name='users/messenger.html'), name='messenger'),
    url(r'^profile/edit$', view=UserUpdateView.as_view(), name='user-update'),

]
