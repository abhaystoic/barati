from django.conf.urls import include, url
from django.contrib import admin
from customers import views

urlpatterns = [
    url(r'^$', views.dashboard.as_view(), name='dashboard'),
    url(r'', include('customers.urls', namespace = 'customers')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    url(r'^user/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
{'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
]
