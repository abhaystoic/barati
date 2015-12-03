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
         self.wishlist_list = []
         self.my_orders = []
         self.order_details_list = []
         self.delivery_status_list = []
      
      def get_context_data(self, **kwargs):
         context = super(My_Orders, self).get_context_data(**kwargs)
         return context
      
      def prepare_my_orders(self, *args, **kwargs):
         request = args[0]
         user_id = m.Users.objects.get(username=request.user.username).id
         orders = m.Orders.objects.filter(user_id=user_id)
         product = None
         if orders:
            for order in orders:
               if order.product_type == 'card':
                  product = m.Cards.objects.get(ref_id=order.ref_id)
                  order_details_of_product = m.Orders.objects.filter(ref_id=order.ref_id)
                  for self.order_details in order_details_of_product:
                     self.delivery_status = m.Delivery_Status.objects.filter(order=self.order_details)
                     self.delivery_status_list.append(self.delivery_status)
                     self.order_details_list.append(self.order_details)
               self.my_orders.append(product)
         return self.my_orders
            
      def get(self, request, **kwargs):
         my_orders = self.prepare_my_orders(request)
         context_dict = {'my_orders' : my_orders, 'order_details' : self.order_details_list, 'delivery_details' : self.delivery_status_list}
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
