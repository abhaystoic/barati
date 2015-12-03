from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from dashboard import Dashboard
from customers import models as m
from django.db import connection, transaction
import sys, json, time, datetime

#@login_required(login_url='/auth/login/')
class Checkout(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/checkout.html'
         self.error_template_name = 'customers/error.html'
         self.cursor = connection.cursor()
      
      def create_package_id(self, ref_id, product_type):
         return str(product_type) + "_" + str(ref_id) + "_" + str(time.time())
         
      def get_context_data(self, request, **kwargs):
         ###To Do : Write logic to implement payment transfer
         try:
            user_id = m.Users.objects.get(username=request.user.username).id
            payment_method = request.POST.get('payment_method')
            query = "SELECT * FROM cart where user_id = {0}".format(user_id)
            products_from_cart = m.Cart.objects.raw(query)
            for product in products_from_cart:
               query = "INSERT INTO orders(ref_id, quantity, total_price, package_id, vendor_acknowledgement, payment_done, payment_received, payment_method, user_id, timestamp, product_type) VALUES('{}', {}, {}, '{}', '{}', '{}', '{}', '{}', {}, {}, '{}')"
               query = query.format(str(product.ref_id), product.quantity, product.total_price, self.create_package_id(product.ref_id, product.product_type), 'pending', 'false', 'false', str(payment_method), user_id, 'now()', 'card')
               self.cursor.execute(query)
               #print self.cursor.lastrowid
               
            first_name = request.POST.get('first_name')
            middlle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            building_number = request.POST.get('building_number')
            street = request.POST.get('street')
            locality = request.POST.get('locality')
            landmark = request.POST.get('landmark')
            address = request.POST.get('address')
            city = request.POST.get('city')
            zipcode = request.POST.get('zipcode')
            phone = request.POST.get('phone')
            
            #Delete everything from cart corresponding to this user_id
            for product in products_from_cart:
               query = "DELETE FROM cart where user_id = {0}"
               query = query.format(user_id)
               self.cursor.execute(query)
         except Exception as general_exception:
            transaction.rollback()
            print general_exception
            print sys.exc_traceback.tb_lineno
            return "error"
         transaction.commit()
         context_dict = super(Checkout, self).get_context_data(**kwargs)
         return context_dict
         
      def get(self, **kwargs):
         context = RequestContext(request)
         context_dict = self.get_context_data(request)
         if context_dict == "error":
            return render(request, self.error_template_name, context_dict)   
         return render(request, self.template_name, context_dict)
         
      def post(self, request, **kwargs):   
         context = RequestContext(request)
         context_dict = self.get_context_data(request)
         if context_dict == "error":
            return render(request, self.error_template_name, context_dict)   
         return render(request, self.template_name, context_dict)

   except Exception as general_exception:
      transaction.rollback()
      print general_exception
      print sys.exc_traceback.tb_lineno
