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
        r'^faq$',
        TemplateView.as_view(template_name='mainapp/faq.html'),
        name='faq'
    ),
    url(
        r'^privacy$',
        TemplateView.as_view(template_name='mainapp/privacy.html'),
        name='privacy'
    ),
    url(
        r'^terms$',
        TemplateView.as_view(template_name='mainapp/terms.html'),
        name='terms'
    ),
    url(
        r'^aboutus$',
        TemplateView.as_view(template_name='mainapp/aboutus.html'),
        name='aboutus'
    ),
    url(
        r'^prepare$',
        TemplateView.as_view(template_name='pages/how-it-works.html'),
        name='prepare'
    ),
    url(
        r'^purchase$',
        TemplateView.as_view(template_name='mainapp/purchase.html'),
        name='purchase'
    ),
    url(
        r'^own$',
        TemplateView.as_view(template_name='mainapp/own.html'),
        name='own'
    ),
]
