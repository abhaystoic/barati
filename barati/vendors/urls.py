from django.conf.urls import patterns, include, url, handler404
from vendors import views

urlpatterns = patterns('',
   url(r'^$', views.dashboard.as_view(), name = 'dashboard'),
   )
