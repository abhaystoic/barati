from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
from django.db import connection, transaction
import sys, json
#A function based view for adding a product in the cart. Returns json data and doesn't refresh the page
#@login_required(login_url='/auth/login/')
def Add_To_Cart(request, ref_id):
   cursor = connection.cursor()
   context_dict = {}
   message = ""
   try:
      context = RequestContext(request)
      product_type = request.POST.get('product_type')
      user_id = request.POST.get('user_id')
      price = int(request.POST.get('price'))
      quantity = int(request.POST.get('quantity'))
      total_price = quantity * price
      checked_out = "false"
      query = "INSERT INTO cart(ref_id, product_type, checked_out, user_id, quantity, total_price) VALUES( '%s', '%s', %s, %d, %d, %d)"\
      %(str(ref_id), str(product_type), str(checked_out), int(user_id), int(quantity), int(total_price))
      cursor.execute(query)
      transaction.commit()
      message = "successfully added in cart"
   except Exception as general_exception:
      message = str(general_exception)
      print general_exception
      print sys.exc_traceback.tb_lineno
   return HttpResponse(json.dumps(message))
