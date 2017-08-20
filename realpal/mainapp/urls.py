from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from realpal.mainapp.views import RegisterPurchaseStep, RegisterMaritalStatus, RegisterFirstHome, RegisterHouseType,\
    RegisterCity, RegisterMaxBudget, RegisterCurrentRent, RegisterHowSoon, RegisterPersonalProfile

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
    url(r'^register/purchase-step$', RegisterPurchaseStep.as_view(), name='register-purchase-step'),
    url(r'^register/marital-status$', RegisterMaritalStatus.as_view(), name='register-marital-status'),
    url(r'^register/first-home$', RegisterFirstHome.as_view(), name='register-first-home'),
    url(r'^register/house-type$', RegisterHouseType.as_view(), name='register-house-type'),
    url(r'^register/city$', RegisterCity.as_view(), name='register-city'),
    url(r'^register/max-budget$', RegisterMaxBudget.as_view(), name='register-max-budget'),
    url(r'^register/current-rent$', RegisterCurrentRent.as_view(), name='register-current-rent'),
    url(r'^register/how-soon$', RegisterHowSoon.as_view(), name='register-how-soon'),
    url(r'^register/personal-profile$', RegisterPersonalProfile.as_view(), name='register-personal-profile'),

    url(
        r'^onboarding/prepare/profile$',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/profile.html'),
        name='prepare-profile'
    ),
    url(
        r'^onboarding/prepare/first-time$',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/is_first_home.html'),
        name='prepare-firsttime'
    ),
    url(
        r'^onboarding/prepare/home-type$',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/home_type.html'),
        name='prepare-hometype'
    ),
    url(
        r'^onboarding/prepare/max-budget',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/max_budget.html'),
        name='prepare-maxbudget'
    ),
    url(
        r'^onboarding/prepare/rent',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/rent.html'),
        name='prepare-rent'
    ),
    url(
        r'^onboarding/prepare/timeline',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/timeline.html'),
        name='prepare-timeline'
    ),
    url(
        r'^onboarding/prepare/house-choice',
        TemplateView.as_view(template_name='mainapp/onboarding_prepare/house_choices.html'),
        name='prepare-housechoice'
    ),
    url(
        r'^onboarding/prepare/areas-choice',
        views.serve_cities,
        name='prepare-areas'
    )
]
