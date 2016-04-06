#Ignore pylint whitespace warning
# pylint: disable=W0311
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View,CreateView
from django.http import HttpResponse
from django.db import connection, transaction
from django.db.models import Sum
from django.contrib.auth.models import User
from django.template.defaulttags import register
from customers.models import Users
import sys, json, os, datetime, decimal
from customers import models as m
from customers.forms import ProfileForm
from customers.forms import AddressForm
from customers.views_cluster.dashboard import Dashboard

#us=""

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

#Get the path of the main pic to be displayed
@register.filter(name = 'get_pic_path') 
def get_pic_path(key):
   try:
      value = m.Product_Pictures.objects.get(name__startswith=(str(key)+'_1')).picture #Using '.get' To suppress key error (just in case)
      return ('images/' + str(value))
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

#Get the paths of the other images of the product
@register.filter(name = 'get_other_pics_path') 
def get_other_pics_path(key):
   try:
      other_pic_list = []
      other_pic_list.extend(m.Product_Pictures.objects.filter(name__contains=(str(key)))) #Using '.get' To suppress key error (just in case)
      del other_pic_list[0] #Delete the main product pic and display only the other pics
      return other_pic_list
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
      vendor_id = m.Beauticians.objects.get(ref_id=ref_id).vendor_id
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

#A Filter for getting tax
@register.filter(name = 'add_tax')
def add_tax(actual_price, tax):
   try:
      value = round(decimal.Decimal(actual_price + actual_price * (tax/100)), 2)
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

@register.filter(name = 'change_date_format_for_template')
def change_date_format_for_template(unformatted_date):
   formatted_date = None
   if unformatted_date:
      formatted_date = datetime.datetime.strptime(str(unformatted_date), '%Y-%m-%d').strftime('%d-%b-%Y')
   return formatted_date

def profile(request):
   us = m.Users.objects.get(username=request.user.username)
   try:
      add = m.Address.objects.get(users_id=us.id)
   except m.Address.DoesNotExist:
      add=None
   if request.POST:
      
      
      form = ProfileForm(request.POST or None,instance=us)
      if not add:
         form1 = AddressForm(data=request.POST,prefix="a",instance=add)
      else:
         form1 = AddressForm(data=request.POST,prefix="a",instance=add)
      a_valid = form.is_valid()
      b_valid = form1.is_valid()
      
      if a_valid and b_valid:
       
         a = form.save()
         b = form1.save(commit=False)
         
         b.save()
         us_add = m.Address.objects.get(id=b.id)
         us_add.users_id = us.id
         us_add.save(update_fields=['users_id'])
      
   else:
      form = ProfileForm(instance=us)
      form1 = AddressForm(instance=add)
   return render(request, 'profile.html', {'form': form,'form1':form1})

