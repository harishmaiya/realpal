from django.conf.urls import url
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='purchase-step'),
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
        TemplateView.as_view(template_name='mainapp/about-us.html'),
        name='aboutus'
    ),
    url(
        r'^prepare$',
        TemplateView.as_view(template_name='home/how-it-works.html'),
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
