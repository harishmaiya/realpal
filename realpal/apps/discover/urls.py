from django.conf.urls import url

from realpal.apps.discover.views import DiscoverView

urlpatterns = [
    url(r'^$', DiscoverView.as_view(), name='latest'),
    url(r'^rent-buy$', DiscoverView.as_view(), name='rent-buy'),
    url(r'^personal-fincance$', DiscoverView.as_view(), name='personal-finance'),
    url(r'^house-select$', DiscoverView.as_view(), name='house-select'),
    url(r'^house-loan$', DiscoverView.as_view(), name='house-loan'),
    url(r'^location$', DiscoverView.as_view(), name='location'),
    url(r'^agent-selection$', DiscoverView.as_view(), name='agent-selection'),
    url(r'^your-journey', DiscoverView.as_view(), name='your-journey'),
    url(r'^(?P<url_name>.+)$', DiscoverView.as_view(), name='param'),
]
