#Ignore pylint whitespace warning
# pylint: disable=W0311

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template.defaulttags import register
import sys
from customers.models import Users as users
from customers.models import Vendors as vendors
from customers.models import Orders as orders
from customers.models import Address

#A Filter for enabling the usage of a dictionary in the templates
@register.filter(name = 'get_full_address')
def get_full_address(address_id):
   try:
      print address_id
      address = Address.objects.get(id=address_id)
      full_address = (str(address.building_number) if address.building_number != None else '') + ' ' +\
         (str(address.street) if address.street != None else '') + ' ' + (str(address.locality) if address.locality != None else '') + ' ' +\
         (str(address.landmark) if address.landmark != None else '') + ' ' + ((', ' + str(address.city)) if address.city != None else '')
      return full_address
   except Exception as general_exception:
      print str(general_exception)
      print "Line number : " + str(sys.exc_traceback.tb_lineno)
      return "not_found"

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
