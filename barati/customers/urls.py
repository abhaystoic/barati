from django.conf.urls import patterns, include, url, handler404
from customers import views 
urlpatterns = patterns('',
   url(r'^$', views.dashboard, name = 'dashboard'),
   url(r'^blog/$', views.blog, name = 'blog'),
   url(r'^cart/$', views.cart, name = 'cart'),
   url(r'^checkout/$', views.checkout, name = 'checkout'),
   url(r'^contact_us/$', views.contact_us, name = 'contact_us'),
   url(r'^product_details/$', views.product_details, name = 'product_details'),
   url(r'^shop/$', views.shop, name = 'shop'),
   )
