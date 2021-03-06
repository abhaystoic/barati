from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
from dashboard import Dashboard
import sys, json

class My_Orders(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/my_orders.html'
         self.product_info_dict = {}
         self.product_type_dict = {}

      def get_context_data(self, **kwargs):
         context = super(My_Orders, self).get_context_data(**kwargs)
         return context
      
      def prepare_my_orders(self, *args, **kwargs):
         request = args[0]
         user_id = m.Users.objects.get(username=request.user.username).id
         orders = m.Orders.objects.filter(user_id=user_id)
         return orders
      
      def prepare_delivery_status(self, *args, **kwargs):
         order = args[0]
         delivery_status = m.Delivery_Status.objects.get(order=order)
         return delivery_status
         
      def prepare_product_details(self, *args, **kwargs):
         ref_id = args[0]
         product_type = args[1]
         product_details = None   
         if product_type == 'card':
            product_details = m.Cards.objects.get(ref_id=ref_id)
            self.product_type_dict.update({ref_id : 'card'})
         if product_type == 'venue':
            product_details = m.Venues.objects.get(ref_id=ref_id)
            self.product_type_dict.update({ref_id : 'venue'})
         if product_type == 'beautician':
            product_details = m.Beauticians.objects.get(ref_id=ref_id)
            self.product_type_dict.update({ref_id : 'beautician'})
         return product_details
            
      def get(self, request, **kwargs):
         delivery_status_dict = {}
         product_details_dict = {}
         all_delivery_statuses_dict = {}
         all_product_details_dict = {}
         
         #Prepare details from Order table for the logged in user
         order_details = self.prepare_my_orders(request)
         context_dict = {'order_details' : order_details}
         
         for order in order_details:
            #Prepare details of Delivery
            delivery_status = self.prepare_delivery_status(order)
            delivery_status_dict.update({'delivery_status_' + str(order.ref_id) : delivery_status})

            #Prepare product details
            product_details = self.prepare_product_details(order.ref_id, order.product_type)
            product_details_dict.update({'product_details_' + str(order.ref_id) : product_details})
         
         user_id = m.Users.objects.get(username= request.user.username).id
         #Get tax percentages 
         super(My_Orders, self).get_each_tax()
         
         context_dict.update(self.get_context_data(request=request))
         context_dict.update({'all_delivery_statuses_dict' : delivery_status_dict , 'all_product_details_dict' : product_details_dict,\
            'product_type_dict' : self.product_type_dict\
         })
         context_dict.update({\
         'tax_venue' : self.tax_venue, 'tax_beautician' : self.tax_beautician, 'tax_gift' : self.tax_gift,\
         'tax_music' : self.tax_music, 'tax_photo_video' : self.tax_photo_video, 'tax_bakery' : self.tax_bakery,\
         'tax_ghodi_bagghi' : self.tax_ghodi_bagghi, 'tax_band' : self.tax_band, 'tax_mehendi' : self.tax_mehendi,\
         'tax_firework' : self.tax_firework, 'tax_card' : self.tax_card
         })
         #print context_dict['all_product_details_dict'], 'sasas'
         return render(request, self.template_name, context_dict)

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
