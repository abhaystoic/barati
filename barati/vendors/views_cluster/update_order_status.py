from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers.models import Users as users
from customers.models import Vendors as vendors
from customers.models import Orders as orders
from customers.models import Address
import sys, json, datetime

class Update_Order_Status(View):
   try:
      
      def post(self, request, order_id):
         context_dict = {}
         orders_list = []
         user = users.objects.get(username=request.user.username)
         #Allow only admin and vendors to see the vendor pages otherwise redirect to the customer index page
         #This is just a precaution here
         if user.role == 'customer':
            self.template_name = 'customers/index.html'
         order = orders.objects.get(order_id=order_id)
         order.vendor_acknowledgement = request.POST.get('status')
         order.last_status_time = datetime.datetime.now()
         order.save()
         message = "success_update_status"
         return HttpResponse(json.dumps(message))
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
