from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.contrib.auth import views as auth_views
import debug_toolbar

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name='home/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # Django resyt
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # User management
    url(r'^account/', include('realpal.apps.users.urls', namespace='users')),
    url(r'^onboarding/', include('realpal.apps.onboarding.urls', namespace='onboarding')),
    # Your stuff: custom urls includes go here
    url(r'^', include('realpal.mainapp.urls', namespace='mainapp')),
    url(r'^chat/', include('realpal.apps.chat.urls', namespace='chat')),
    url(r'^discover/', include('realpal.apps.discover.urls', namespace='discover')),

    # these view will deal with password resetting
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
# This allows the error home to be debugged during development, just visit
# these url in browser to see how these error home look like.
    urlpatterns += [
url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
url(r'^500/$', default_views.server_error),
]

urlpatterns = [
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
