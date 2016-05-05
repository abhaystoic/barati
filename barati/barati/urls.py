from django.conf.urls import include, url
from django.contrib import admin
from customers.views_cluster.dashboard import Dashboard
from vendors import views as vendors_views

urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='dashboard'),
    url(r'', include('customers.urls', namespace = 'customers')),
    url(r'^vendor/', include('vendors.urls', namespace = 'vendors')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
{'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout_then_login/',  'django.contrib.auth.views.logout_then_login', {'login_url': '/auth/login/'}),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^calendar/1', include('happenings.urls', namespace='calendar')),
]
