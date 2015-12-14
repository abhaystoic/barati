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
@login_required(login_url='/auth/login/')
def Add_To_Cart(request, ref_id):
   cursor = connection.cursor()
   context_dict = {}
   message = ""
   try:
      context = RequestContext(request)
      product_type = request.POST.get('product_type')
      avail_printing = request.POST.get('avail_printing_checkbox')
      card_printing_price_per_card = 0
      if request.POST.get('card_printing_price_per_card') is not None:
         card_printing_price_per_card = float(request.POST.get('card_printing_price_per_card'))
      if avail_printing == None:
         avail_printing = False
      else:
         avail_printing = True   
      user_id = m.Users.objects.get(username=request.user.username).id
      price = int(request.POST.get('price'))
      quantity = None
      total_price = None
      if request.POST.get('quantity') is not None:
         quantity = int(request.POST.get('quantity'))
         #Add printing cost
         if avail_printing == True:
            total_price = quantity * price + quantity * card_printing_price_per_card
         else:
            total_price = quantity * price   
      else:
         #Quantity is irrelevant here but need to give a 1 value to maintain uniform
         quantity = 1
         total_price = price
      checked_out = "false"
      query = "INSERT INTO cart(ref_id, product_type, checked_out, user_id, quantity, total_price) VALUES( '{}', '{}', '{}', {}, {}, {})".format(str(ref_id), str(product_type), str(checked_out), int(user_id), quantity, total_price)
      cursor.execute(query)
      if product_type == 'card':
         card_id = m.Cards.objects.get(ref_id=ref_id).id
         existing_preference_check = m.Cards_Preferences.objects.filter(ref_id=ref_id, user_id=user_id).exists()
         #If card preference exists then update else create new
         if existing_preference_check:
            existing_preference_card = m.Cards_Preferences.objects.get(ref_id=ref_id, user_id=user_id)
            existing_preference_card.avail_printing = avail_printing
            existing_preference_card.save()
         else:
            m.Cards_Preferences(ref_id=ref_id, avail_printing=avail_printing, card_id=card_id, user_id=user_id).save()
      transaction.commit()
      message = "success_add_to_cart"
      return HttpResponse(json.dumps(message))   
   except Exception as general_exception:
      message = str(general_exception)
      print general_exception
      print sys.exc_traceback.tb_lineno
      return HttpResponse(json.dumps(message))
