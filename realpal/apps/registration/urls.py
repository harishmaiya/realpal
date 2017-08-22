from django.conf.urls import url
from django.views.generic import TemplateView
from .views import PurchaseStepView, MaritalStatusView, FirstHomeView,\
    HouseTypeView, CityView, MaxBudgetView, CurrentRentView, HowSoonView, PersonalProfileView

urlpatterns = [
    url(r'^purchase-step$', PurchaseStepView.as_view(), name='purchase-step'),
    url(r'^marital-status$', MaritalStatusView.as_view(), name='marital-status'),
    url(r'^first-home$', FirstHomeView.as_view(), name='first-home'),
    url(r'^house-type$', HouseTypeView.as_view(), name='house-type'),
    url(r'^city$', CityView.as_view(), name='city'),
    url(r'^max-budget$', MaxBudgetView.as_view(), name='max-budget'),
    url(r'^current-rent$', CurrentRentView.as_view(), name='current-rent'),
    url(r'^how-soon$', HowSoonView.as_view(), name='how-soon'),
    url(r'^personal-profile$', PersonalProfileView.as_view(), name='personal-profile'),
    url(
        r'^activation-error$',
        TemplateView.as_view(template_name='registration/activation_error.html'),
        name='activation-error'
    ),
]
