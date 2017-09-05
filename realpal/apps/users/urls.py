from django.conf.urls import url
from django.views.generic import TemplateView
from .views import UserUpdateView, UserListView, UserDetailView, UserRedirectView, Login, Logout

urlpatterns = [
    url(r'^$', view=UserUpdateView.as_view(), name='update'),
    url(r'login/$', view=Login.as_view(), name='login'),
    url(r'logout/$', view=Logout.as_view(), name='logout'),
    url(r'^messenger$', TemplateView.as_view(template_name='users/messenger.html'), name='messenger'),
    url(r'^(?P<username>.*)/$', view=UserDetailView.as_view(), name='detail'),
    url(r'~redirect/$', view=UserRedirectView.as_view(), name='redirect'),
]
