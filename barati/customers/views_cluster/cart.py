from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard
from django.db import connection, transaction

#@login_required(login_url='/auth/login/')
class Cart(Dashboard, View):
   try:
      def __init__(self):
         self.cursor = connection.cursor()
         self.template_name = 'customers/cart.html'

      def get_context_data(self, **kwargs):
         context = super(Cart, self).get_context_data(**kwargs)
         return context
      
      def get_queryset(self, *args, **kwargs):
         request = args[0]
         user_id = m.Users.objects.get(username=request.user.username).id
         query_cart = "select distinct on (ref_id) id, ref_id from cart where user_id = " + str(user_id)

         self.cart = m.Cart.objects.raw(query_cart)
         self.card_list = []
         self.venue_list = []
         self.beautician_list = []
         self.music_list = []
         self.gift_list = []
         self.photo_video_list = []
         self.bakery_list = []
         self.ghodi_bagghi_list = []
         self.band_list = []
         self.mehendi_list = []
         self.fireworks_list = []
         self.tent_house_list = []
         
         self.grand_total = 0
         avail_printing = None
         printing_preference_dict = {}
         
         for product in self.cart:
            #Get the details
            query_prod = "select * from " + str(product.product_type) + " where ref_id = '" + str(product.ref_id) + "'"
            
            if str(product.product_type) == "card":
               self.card_list.append(m.Cards.objects.get(ref_id = str(product.ref_id)))
               existing_preference_check = m.Cards_Preferences.objects.filter(ref_id=product.ref_id, user_id=user_id).exists()
               #If card preference exists then update else create new
               if existing_preference_check:
                  avail_printing = m.Cards_Preferences.objects.get(ref_id=product.ref_id, user_id=user_id).avail_printing
                  printing_preference_dict.update({product.ref_id : avail_printing})

            if str(product.product_type) == "venue":
               self.venue_list.append(m.Venues.objects.get(ref_id = str(product.ref_id)))

            if str(product.product_type) == "beautician":
               self.beautician_list.append(m.Beauticians.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "music":
               self.music_list.append(m.Music.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "gift":
               self.gift_list.append(m.Gifs.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "photo_video":
               self.photo_video_list.append(m.Photos_Videos.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "bakery":
               self.bakery_list.append(m.Bakeries.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "ghodi_bagghi":
               self.ghodi_bagghi_list.append(m.Ghodis_Bagghi.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "band":
               self.band_list.append(m.Bands.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "mehendi":
               self.mehendi_list.append(m.Mehendi.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "firework":
               self.fireworks_list.append(m.Fireworks.objects.get(ref_id = str(product.ref_id)))
         
         #Get tax percentages. This also calculates self.tax
         super(Cart, self).get_each_tax()
         self.grand_total = super(Cart, self).calculate_grand_total(user_id)
         
         #"self.tax" comes from the Dashboard class
         self.prod_dict = {'card_list' : self.card_list, 'printing_preference_dict' : printing_preference_dict, 'venue_list' : self.venue_list, 'beautician_list' : self.beautician_list, \
            'music_list' : self.music_list, 'gift_list' : self.gift_list, 'photo_video_list' : self.photo_video_list, \
            'bakery_list' : self.bakery_list, 'ghodi_bagghi_list' : self.ghodi_bagghi_list, 'band_list' : self.band_list, \
            'mehendi_list' : self.mehendi_list, 'fireworks_list' : self.fireworks_list, \
            'grand_total' : self.grand_total,\
            'tax_venue' : self.tax_venue, 'tax_beautician' : self.tax_beautician, 'tax_gift' : self.tax_gift,\
            'tax_music' : self.tax_music, 'tax_photo_video' : self.tax_photo_video, 'tax_bakery' : self.tax_bakery,\
            'tax_ghodi_bagghi' : self.tax_ghodi_bagghi, 'tax_band' : self.tax_band, 'tax_mehendi' : self.tax_mehendi,\
            'tax_firework' : self.tax_firework, 'tax_card' : self.tax_card, 'total_tax_payable' : self.tax
            }
         return self.prod_dict
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         context_dict = self.get_queryset(request)
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)   
   
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
