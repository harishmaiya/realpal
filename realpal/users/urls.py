from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name='home'
    ),
    url(
        r'^messenger$',
        TemplateView.as_view(template_name='users/messenger.html'),
        name='messenger'
    ),

]
