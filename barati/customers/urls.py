from django.conf.urls import patterns, include, url, handler404
from django.contrib.auth.decorators import login_required
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
   url(r'^cart/$', login_required(Cart.as_view()), name = 'cart'),
   url(r'^checkout/$', Checkout.as_view(), name = 'checkout'),
   url(r'^add_to_wishlist/$', login_required(Add_To_Wishlist.as_view()), name = 'add_to_wishlist'),
   url(r'^remove_from_wishlist/(?P<ref_id>[-\w]+)$', login_required(Remove_From_Wishlist.as_view()), name = 'remove_from_wishlist'),
   url(r'^remove_from_cart/(?P<ref_id>[-\w]+)$', login_required(Remove_From_Cart.as_view()), name = 'remove_from_cart'),
   url(r'^my_orders/$', login_required(My_Orders.as_view()), name = 'my_orders'),
   url(r'^wishlist/$', login_required(Wishlist.as_view()), name = 'wishlist'),
   url(r'^submit_review/$', login_required(Submit_Review.as_view()), name = 'submit_review'),
   url(r'^contact_us/$', Contact_Us, name = 'contact_us'),
   url(r'^sign_up/$', Sign_Up.as_view(), name = 'sign_up'),
   url(r'^product_details/$', Product_Details, name = 'product_details'),
   url(r'^venue/(?P<type>[-\w]+)$', Venue.as_view(), name = 'venue'),
   url(r'^card/(?P<type>[-\w]+)$', Card.as_view(), name = 'card'),
   url(r'^beauticians/(?P<type>[-\w]+)$', Beautician.as_view(), name = 'beautician'),
   url(r'^card_details/(?P<card_id>[-\w]+)$', Card_Details.as_view(), name = 'card_details'),
   url(r'^add_to_cart/(?P<ref_id>[-\w]+)$', Add_To_Cart, name = 'add_to_cart'),
   url(r'^shop/$', Shop, name = 'shop'),
   )
