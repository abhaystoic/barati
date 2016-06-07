from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
from customers.models import Users as users
from customers.models import Vendors as vendors
from customers.models import Orders as orders
from customers.models import Product_Availability as product_availability
from customers.models import Address
import sys, json
import ast

class Dashboard(View):
   try:
      template_name = 'vendors/dashboard.html'
      
      def get(self, request):
         context_dict = {}
         orders_list = []
         json_data=[]
         user = users.objects.get(username=request.user.username)
         #Allow only admin and vendors to see the vendor pages otherwise redirect to the customer index page
         if user.role == 'customer':
            self.template_name = 'customers/index.html'
         vendor_id = vendors.objects.get(user_id=user.id).id
         products = product_availability.objects.filter(vendor=vendor_id).values('title','start_date','start_time','end_date','end_time')
         book_products=""
         if products:
            for product in products:
               book_products=book_products + "{start : '"+str(product['start_date'])+"T"+str(product['start_time'])+"',"+'end :' +"'"+str(product['end_date'])+"T"+str(product['end_time'])+"',"+'title :'+ "'"+str(product['title'])+"'},"
         else:
            book_products=None
         context_dict.update({
            'orders' : orders.objects.filter(vendor=vendor_id),
            'book_products' : book_products
             
          })
         return render(request, self.template_name, context_dict)
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
