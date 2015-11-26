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
from django.db.models import Sum

#@login_required(login_url='/auth/login/')
class Cart(Dashboard, View):
   try:
      def __init__(self):
         self.cursor = connection.cursor()
         self.template_name = 'customers/cart.html'

      def get_context_data(self, **kwargs):
         context = super(Cart, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs):
         query_cart = "select distinct on (ref_id) id, ref_id from cart where user_id = 1"

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
         self.tax = None
         self.grand_total = None
         
         for product in self.cart:
            #Get the details
            query_prod = "select * from " + str(product.product_type) + " where ref_id = '" + str(product.ref_id) + "'"
            
            if str(product.product_type) == "cards":
               self.card_list.append(m.Cards.objects.get(ref_id = str(product.ref_id)))

            if str(product.product_type) == "venues":
               self.venue_list.append(m.Venues.objects.get(ref_id = str(product.ref_id)))

            if str(product.product_type) == "beauticians":
               self.beautician_list.append(m.Beauticians.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "music":
               self.music_list.append(m.Music.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "gifts":
               self.gift_list.append(m.Gifs.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "photos_videos":
               self.photo_video_list.append(m.Photos_Videos.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "bakeries":
               self.bakery_list.append(m.Bakeries.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "ghodis_bagghis":
               self.ghodi_bagghi_list.append(m.Ghodis_Bagghi.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "bands":
               self.band_list.append(m.Bands.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "mehendi":
               self.mehendi_list.append(m.Mehendi.objects.get(ref_id = str(product.ref_id)))
               
            if str(product.product_type) == "fireworks":
               self.fireworks_list.append(m.Fireworks.objects.get(ref_id = str(product.ref_id)))
         
         self.cart_sub_total = m.Cart.objects.filter(user_id = 1).aggregate(cart_sub_total = Sum('total_price'))
         if self.cart_sub_total['cart_sub_total'] is not None:
            self.tax = self.cart_sub_total['cart_sub_total'] * 0.10
            self.grand_total = float(self.tax) + float(self.cart_sub_total['cart_sub_total'])
         self.prod_dict = {'card_list' : self.card_list, 'venue_list' : self.venue_list, 'beautician_list' : self.beautician_list, \
            'music_list' : self.music_list, 'gift_list' : self.gift_list, 'photo_video_list' : self.photo_video_list, \
            'bakery_list' : self.bakery_list, 'ghodi_bagghi_list' : self.ghodi_bagghi_list, 'band_list' : self.band_list, \
            'mehendi_list' : self.mehendi_list, 'fireworks_list' : self.fireworks_list, \
            'cart_sub_total' : self.cart_sub_total['cart_sub_total'], 'tax' : self.tax, 'grand_total' : self.grand_total}
         return self.prod_dict
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         context_dict = self.get_queryset()
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)   
   
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
