from django.conf.urls import url
from django.views.generic import TemplateView
from .views import UserUpdateView, UserListView, UserDetailView

urlpatterns = [
    url(r'^$', UserListView.as_view(), name='list'),
    url(r'^messenger$', TemplateView.as_view(template_name='users/messenger.html'), name='messenger'),
    url(r'^edit$', view=UserUpdateView.as_view(), name='edit'),
    url(r'^(?P<username>.*)/$', view=UserDetailView.as_view(), name='detail'),
]
