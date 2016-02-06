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
   url(r'^budget/$', login_required(Budget.as_view()), name = 'budget'),
   url(r'^venues/(?P<type>[-\w]+)$', Venue.as_view(), name = 'venue'),
   url(r'^card/(?P<type>[-\w]+)$', Card.as_view(), name = 'card'),
   url(r'^beauticians/(?P<type>[-\w]+)$', Beautician.as_view(), name = 'beautician'),

   url(r'^card_details/(?P<card_id>[-\w]+)$', Card_Details.as_view(), name = 'card_details'),
   url(r'^beautician_details/(?P<beautician_id>[-\w]+)$', Beautician_Details.as_view(), name = 'beautician_details'),
   url(r'^venue_details/(?P<venue_id>[-\w]+)$', Venue_Details.as_view(), name = 'venue_details'),
   
   url(r'^add_to_cart/(?P<ref_id>[-\w]+)$', Add_To_Cart, name = 'add_to_cart'),
   url(r'^save_budget_preferences/$', login_required(Save_Budget_Preferences.as_view()), name = 'save_budget_preferences'),
   url(r'^save_main_preferences/$', Save_Main_Preferences.as_view(), name = 'save_main_preferences'),
   #url(r'^search/$', include('haystack.urls')),
   url(r'^search/$', Search.as_view(), name = 'search'),
   url(r'^search_everything/$', Search_Everything.as_view(), name = 'search_everything'),
   url(r'^shop/$', Shop, name = 'shop'),
   )
   
   
'''
url(r'^ghodi_bagghi/(?P<type>[-\w]+)$', Ghodi_Bagghi.as_view(), name = 'ghodi_bagghi'),
url(r'^gift/(?P<type>[-\w]+)$', Gift.as_view(), name = 'gift'),
url(r'^music/(?P<type>[-\w]+)$', Music.as_view(), name = 'music'),
url(r'^firework/(?P<type>[-\w]+)$', Firework.as_view(), name = 'firework'),
url(r'^tent/(?P<type>[-\w]+)$', Tent.as_view(), name = 'tent'),
url(r'^photo_video/(?P<type>[-\w]+)$', Photo_Video.as_view(), name = 'photo_video'),
url(r'^band/(?P<type>[-\w]+)$', Band.as_view(), name = 'band'),
'''
'''
url(r'^ghodi_bagghi_details/(?P<ghodi_bagghi_id>[-\w]+)$', Ghodi_Bagghi_Details.as_view(), name = 'ghodi_bagghi_details'),
url(r'^gift_details/(?P<gift_id>[-\w]+)$', Gift_Details.as_view(), name = 'gift_details'),
url(r'^music_details/(?P<music_id>[-\w]+)$', Music_Details.as_view(), name = 'music_details'),
url(r'^firework_details/(?P<firework_id>[-\w]+)$', Firework_Details.as_view(), name = 'firework_details'),
url(r'^tent_details/(?P<tent_id>[-\w]+)$', Tent_Details.as_view(), name = 'tent_details'),
url(r'^photo_video_details/(?P<photo_video_id>[-\w]+)$', Photo_Video_Details.as_view(), name = 'photo_video_details'),
url(r'^band_details/(?P<band_id>[-\w]+)$', Band_Details.as_view(), name = 'band_details'),
'''
