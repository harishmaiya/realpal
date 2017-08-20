from django.conf.urls import url
from registration.views import RegisterPurchaseStep, RegisterMaritalStatus, RegisterFirstHome, RegisterHouseType,\
    RegisterCity, RegisterMaxBudget, RegisterCurrentRent, RegisterHowSoon, RegisterPersonalProfile


urlpatterns = [
    url(r'^purchase-step$', RegisterPurchaseStep.as_view(), name='purchase-step'),
    url(r'^marital-status$', RegisterMaritalStatus.as_view(), name='marital-status'),
    url(r'^first-home$', RegisterFirstHome.as_view(), name='first-home'),
    url(r'^house-type$', RegisterHouseType.as_view(), name='house-type'),
    url(r'^city$', RegisterCity.as_view(), name='city'),
    url(r'^max-budget$', RegisterMaxBudget.as_view(), name='max-budget'),
    url(r'^current-rent$', RegisterCurrentRent.as_view(), name='current-rent'),
    url(r'^how-soon$', RegisterHowSoon.as_view(), name='how-soon'),
    url(r'^personal-profile$', RegisterPersonalProfile.as_view(), name='personal-profile'),
]
