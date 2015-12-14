#Ignore pylint whitespace warning
# pylint: disable=W0311
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.db import connection, transaction
from django.db.models import Sum
from django.contrib.auth.models import User
from django.template.defaulttags import register
from customers import models as m
import sys, json, os

from customers.views_cluster.dashboard import Dashboard

def get_categories():
   categories = ('venues', 'cards', 'beauticians', 'gifts', 'photo_videos', 'bakeries', 'ghodi_bagghis', 'bands', 'mehendis', 'fireworks', 'tents', 'music')
   return categries
      
#Importing all the clustered views
dir_name = 'customers.views_cluster.'
file_list = os.listdir(os.path.dirname(__file__) + '/views_cluster')
for files in file_list:
   mod_name,file_ext = os.path.splitext(os.path.split(files)[-1])
   if file_ext.lower() == '.py':
      if mod_name != '__init__':
         exec "from {0} import {1}".format(dir_name + files.split(".")[0], files.split(".")[0].title())

#A Filter for enabling the usage of a dictionary in the templates
@register.filter(name = 'get_item') 
def get_item(dictionary, key):
   try:
      value = dictionary.get(key) #Using '.get' To suppress key error (just in case)
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"      

#A Filter for enabling the usage of a dictionary in the templates
@register.filter(name = 'get_user')
def get_user(username):
   try:
      user = User.objects.get(username=username)
      name = user.first_name + " " + user.last_name
      return name
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

#Special filter for My Orders page
@register.filter(name = 'get_item_for_my_orders') 
def get_item_for_my_orders(dictionary, key):
   try:
      value = dictionary.get(key) #Using '.get' To suppress key error (just in case)
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

#Filter for cart
@register.filter(name = 'get_pic_path') 
def get_pic_path(key):
   try:
      value = m.Product_Pictures.objects.get(ref_id = key).picture_path #Using '.get' To suppress key error (just in case)
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

#Filter for cart
@register.filter(name = 'get_quantity')
def get_quantity(key, request):
   try:
      total_quantity = 0
      user_id = m.Users.objects.get(username=request.user.username).id
      quantities = m.Cart.objects.filter(ref_id = key, user_id=user_id)
      for quantity in quantities:
         if quantity.quantity is not None:
            total_quantity = total_quantity + quantity.quantity
      return total_quantity
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return 0

@register.filter(name = 'get_beautician')
def get_beautician(ref_id):
   try:
      vendor_id = m.Beauticians.objects.get(ref_id=ref_id).vendor_id_id
      beautician = m.Vendors.objects.get(id=vendor_id)
      beautician_name = beautician.name
      locality = m.Address.objects.get(id=beautician.address_id).locality
      return (beautician_name, locality)
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return 0

#Filter for cart
@register.filter(name = 'get_total_price')
def get_total_price(key, request):
   try:
      user_id = m.Users.objects.get(username=request.user.username).id
      cart = m.Cart.objects.filter(ref_id = key, user_id=user_id).aggregate(sum_total = Sum('total_price'))
      return cart['sum_total']
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return 0


#A Filter for multiplication
@register.filter(name = 'multiply')
def multiply(first, second):
   try:
      value = first * second
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

@register.filter(name = 'decrement') 
def decrement(value):
   try:
      value = value - 1
      return value
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"
