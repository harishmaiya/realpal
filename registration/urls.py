from django.conf.urls import url
from registration.views import RegisterPurchaseStep, RegisterMaritalStatus, RegisterFirstHome, RegisterHouseType,\
    RegisterCity, RegisterMaxBudget, RegisterCurrentRent, RegisterHowSoon, RegisterPersonalProfile


urlpatterns = [
    url(r'^register/purchase-step$', RegisterPurchaseStep.as_view(), name='purchase-step'),
    url(r'^register/marital-status$', RegisterMaritalStatus.as_view(), name='marital-status'),
    url(r'^register/first-home$', RegisterFirstHome.as_view(), name='first-home'),
    url(r'^register/house-type$', RegisterHouseType.as_view(), name='house-type'),
    url(r'^register/city$', RegisterCity.as_view(), name='city'),
    url(r'^register/max-budget$', RegisterMaxBudget.as_view(), name='max-budget'),
    url(r'^register/current-rent$', RegisterCurrentRent.as_view(), name='current-rent'),
    url(r'^register/how-soon$', RegisterHowSoon.as_view(), name='how-soon'),
    url(r'^register/personal-profile$', RegisterPersonalProfile.as_view(), name='personal-profile'),
]
