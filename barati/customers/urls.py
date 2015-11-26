from django.conf.urls import patterns, include, url, handler404
from customers import views
import os
#Importing all the clustered views
dir_name = 'customers.views_cluster.'
file_list = os.listdir(os.path.dirname(__file__) + '/views_cluster')
for files in file_list:
   mod_name,file_ext = os.path.splitext(os.path.split(files)[-1])
   if file_ext.lower() == '.py':
      if mod_name != 'prepare_context' and  mod_name != '__init__':
         exec "from {0} import {1}".format(dir_name + files.split(".")[0], files.split(".")[0].title())

urlpatterns = patterns('',
   url(r'^$', Dashboard.as_view(), name = 'dashboard'),
   url(r'^dashboard/$', Dashboard.as_view(), name = 'dashboard'),
   url(r'^blog/$', Blog, name = 'blog'),
   url(r'^cart/$', Cart.as_view(), name = 'cart'),
   url(r'^checkout/$', Checkout.as_view(), name = 'checkout'),
   url(r'^contact_us/$', Contact_Us, name = 'contact_us'),
   url(r'^product_details/$', Product_Details, name = 'product_details'),
   url(r'^venue/(?P<type>[-\w]+)$', Venue.as_view(), name = 'venue'),
   url(r'^card/(?P<type>[-\w]+)$', Card.as_view(), name = 'card'),
   url(r'^card_details/(?P<card_id>[-\w]+)$', Card_Details.as_view(), name = 'card_details'),
   url(r'^add_to_cart/(?P<ref_id>[-\w]+)$', Add_To_Cart, name = 'add_to_cart'),
   url(r'^shop/$', Shop, name = 'shop'),
   )
