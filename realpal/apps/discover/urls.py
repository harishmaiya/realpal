from django.conf.urls import url

from realpal.apps.discover.views import DiscoverView

urlpatterns = [
    url(r'^$', DiscoverView.as_view(), name='latest'),
]
