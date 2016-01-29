from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url, handler404
from vendors import views
import os
#Importing all the clustered views
dir_name = 'vendors.views_cluster.'
file_list = os.listdir(os.path.dirname(__file__) + '/views_cluster')
for files in file_list:
   mod_name,file_ext = os.path.splitext(os.path.split(files)[-1])
   if file_ext.lower() == '.py':
      if mod_name != '__init__':
         exec "from {0} import {1}".format(dir_name + files.split(".")[0], files.split(".")[0].title())

urlpatterns = patterns('',
   url(r'^$', login_required(Dashboard.as_view()), name = 'dashboard'),
   url(r'^queued_orders/$', login_required(Queued_Orders.as_view()), name = 'queued_orders'),
   url(r'^active_orders/$', login_required(Active_Orders.as_view()), name = 'active_orders'),
   url(r'^completed_orders/$', login_required(Completed_Orders.as_view()), name = 'completed_orders'),
   url(r'^queued_orders/$', login_required(Queued_Orders.as_view()), name = 'queued_orders'),
   url(r'^inprogress_orders/$', login_required(Inprogress_Orders.as_view()), name = 'inprogress_orders'),
   url(r'^confirm_order/(?P<order_id>[-\w]+)$', login_required(Confirm_Order.as_view()), name = 'confirm_order'),
   url(r'^cancel_order/(?P<order_id>[-\w]+)$', login_required(Cancel_Order.as_view()), name = 'cancel_order'),
   url(r'^update_order_status/(?P<order_id>[-\w]+)$', login_required(Update_Order_Status.as_view()), name = 'update_order_status'),
   url(r'^list_product/$', login_required(List_Product.as_view()), name = 'list_product'),
   )
