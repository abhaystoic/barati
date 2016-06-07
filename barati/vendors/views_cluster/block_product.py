from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json

class Block_Product(View):
   try:
      def __init__(self):
         self.template_name = ''
         
      def post(self, request, **kwargs):
         try:
            user = m.Users.objects.get(username=request.user.username).id
            vendor_id =  m.Vendors.objects.get(user_id=user).id
            product_id = request.POST.get('product_id')
            title = request.POST.get('title')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            product = m.Product_Availability(vendor_id=vendor_id, ref_id=product_id, title=title,start_date=start_date,end_date=end_date,start_time=start_time,end_time=end_time)
            product.save()
            message="success_submit"
         except Exception as general_exception:
            message = str(general_exception)
            print general_exception
            print sys.exc_traceback.tb_lineno
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno