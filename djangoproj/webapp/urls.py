from django.conf.urls import url
from webapp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), 
    url(r'^prepare/$', views.PreparePageView.as_view(), name='prepare'),
    url(r'^buy/$', views.BuyPageView.as_view(), name='buy'),
    url(r'^live/$', views.LivePageView.as_view(), name='live'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^login/$', views.LoginPageView.as_view(), name='login'),
]
