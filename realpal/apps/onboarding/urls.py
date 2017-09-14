from django.conf.urls import url
from django.views.generic import TemplateView
from .views import MaritalStatusView, FirstHomeView,\
    HouseTypeView, CityView, MaxBudgetView, HowSoonView, PersonalProfileView, ActivateAccount,\
    ResendActivationEmail

urlpatterns = [
    url(r'^prepare/family$', MaritalStatusView.as_view(), name='marital-status'),
    url(r'^prepare/first-home$', FirstHomeView.as_view(), name='first-home'),
    url(r'^prepare/house-type$', HouseTypeView.as_view(), name='house-type'),
    url(r'^prepare/city$', CityView.as_view(), name='city'),
    url(r'^prepare/max-budget$', MaxBudgetView.as_view(), name='max-budget'),
    url(r'^prepare/how-soon$', HowSoonView.as_view(), name='how-soon'),
    url(r'^prepare/personal-profile$', PersonalProfileView.as_view(), name='personal-profile'),
    url(r'^prepare/activate/(?P<uuid>.*)/$', ActivateAccount.as_view(), name='activate-account'),
    url(r'^resend/$', ResendActivationEmail.as_view(), name='resend'),
    url(
        r'^activation-error$',
        TemplateView.as_view(template_name='onboarding/activation_error.html'),
        name='activation-error'
    ),
]
