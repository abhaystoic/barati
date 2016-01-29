from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers.models import Users as users
from customers.models import Vendors as vendors
from customers.models import Orders as orders
from customers.models import Address
import sys, json

class List_Product(View):
   try:
      template_name = 'vendors/list_product.html'
      
      def get(self, request):
         context_dict = {}
         orders_list = []
         user = users.objects.get(username=request.user.username)
         #Allow only admin and vendors to see the vendor pages otherwise redirect to the customer index page
         if user.role == 'customer':
            self.template_name = 'customers/index.html'
         return render(request, self.template_name, context_dict)
   except Exception as e:
      print e
      print sys.exc_traceback.tb_lineno
