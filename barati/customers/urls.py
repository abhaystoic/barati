from django.conf.urls import patterns, include, url, handler404
from customers import views

urlpatterns = patterns('',
   url(r'^$', views.Dashboard.as_view(), name = 'dashboard'),
   url(r'^dashboard/$', views.Dashboard.as_view(), name = 'dashboard'),
   url(r'^blog/$', views.blog, name = 'blog'),
   url(r'^cart/$', views.Cart.as_view(), name = 'cart'),
   url(r'^checkout/$', views.checkout, name = 'checkout'),
   url(r'^contact_us/$', views.contact_us, name = 'contact_us'),
   url(r'^product_details/$', views.product_details, name = 'product_details'),
   url(r'^venue/(?P<type>[-\w]+)$', views.Venue.as_view(), name = 'venue'),
   url(r'^card/(?P<type>[-\w]+)$', views.Card.as_view(), name = 'card'),
   url(r'^card_details/(?P<card_id>[-\w]+)$', views.Card_Details.as_view(), name = 'card_details'),
   url(r'^add_to_cart/(?P<ref_id>[-\w]+)$', views.add_to_cart, name = 'add_to_cart'),
   url(r'^shop/$', views.shop, name = 'shop'),
   )
