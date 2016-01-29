from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json, datetime, decimal
from django.db.models import Sum
#@login_required(login_url='/auth/login/')
class Dashboard(View):
   try:
      def __init__(self):
         self.template_name = 'customers/index.html'

      def get_tax(self, product_type):
         return m.Tax_And_Refund_Policies.objects.filter(product_type=product_type)[0].total_tax

      def get_each_tax(self):
         
         self.tax_venue = 0
         self.tax_beautician = 0
         self.tax_gift = 0
         self.tax_music = 0
         self.tax_photo_video = 0
         self.tax_bakery = 0
         self.tax_ghodi_bagghi = 0
         self.tax_band = 0
         self.tax_mehendi = 0
         self.tax_firework = 0
         self.tax_card = 0
         
         self.tax_venue = self.get_tax('venue')
         self.tax_beautician = self.get_tax('beautician')
         self.tax_card = self.get_tax('card')
         
         return
          
      def calculate_grand_total(self, user_id):
         self.grand_total = None
         self.tax = 0 #Stores total payable tax amount in rs
         self.grand_total = m.Cart.objects.filter(user_id = user_id).aggregate(grand_total = Sum('total_price'))
         
         #Calculating tax amount
         cart_products = m.Cart.objects.filter(user_id = user_id)
         if cart_products is not None:
            for product in cart_products:
               self.tax = self.tax + self.get_tax(product.product_type)
         if self.grand_total['grand_total']:
            return float(self.grand_total['grand_total'])
         else:
            return None
         
      def get_context_data(self, **kwargs):
         
         request = None
         if kwargs is not None:
            for key, value in kwargs.iteritems():
               if key == 'request':
                  request = value
         budget = None
         grand_total = None
         budget_balance = None
         main_preferences = None
         query = "select id, name from venue_types"
         venue_types = m.Venue_Types.objects.raw(query)
         
         query = "select id, name from card_types"
         card_types = m.Card_Types.objects.raw(query)
         
         query = "select id, name from beautician_types"
         beautician_types = m.Beautician_Types.objects.raw(query)
         
         query = "select id, name from music_types"
         music_types = m.Music_Types.objects.raw(query)
         
         query = "select id, name from gift_types"
         gift_types = m.Gift_Types.objects.raw(query)
         
         query = "select id, name from photo_video_types"
         photo_video_types = m.Photo_Video_Types.objects.raw(query)
         
         query = "select id, name from bakery_types"
         bakery_types = m.Bakery_Types.objects.raw(query)
         
         query = "select id, name from ghodi_bagghi_types"
         ghodi_bagghi_types = m.Ghodi_Bagghi_Types.objects.raw(query)
         
         query = "select id, name from band_types"
         band_types = m.Band_Types.objects.raw(query)
         
         query = "select id, name from mehendi_types"
         mehendi_types = m.Mehendi_Types.objects.raw(query)
         
         query = "select id, name from fireworks_types"
         fireworks_types = m.Fireworks_Types.objects.raw(query)
         
         query = "select id, name from tent_types"
         tent_types = m.Tent_Types.objects.raw(query)
         
         #Pull data for Budgeting Tool and main preferences if the user is logged in
         if request is not None and request.user.username:
            user_id = m.Users.objects.get(username=request.user.username).id
            if user_id:
               query = "select id, min_master, max_master from budget where user_id = {}".format(str(user_id))
               budget = m.Budget.objects.raw(query)
               grand_total = self.calculate_grand_total(user_id)
               if grand_total and len(list(budget)) !=0 and budget[0].max_master:
                  if grand_total <= float(budget[0].max_master):
                     budget_balance = (float(budget[0].max_master - grand_total), 0)
                  elif grand_total > float(budget[0].max_master):
                     budget_balance = (float(grand_total - budget[0].max_master), 1)
                     
               query = "select id, date, location, sublocation from main_preferences where user_id = {}".format(str(user_id))
               main_preferences = m.Main_Preferences.objects.raw(query)
         context = {\
         'venue_types' : venue_types, 'card_types' : card_types, 'beautician_types' : beautician_types,\
         'gift_types' : gift_types, 'photo_video_types' : photo_video_types,\
         'bakery_types' : bakery_types, 'ghodi_bagghi_types' : ghodi_bagghi_types,\
         'band_types' : band_types, 'mehendi_types' : mehendi_types, 'fireworks_types' : fireworks_types,\
         'tent_types' : tent_types, 'music_types' : music_types, 'budget' : budget, 'budget_balance' : budget_balance, \
         'grand_total' : grand_total, 'main_preferences' : main_preferences \
         }
         return context
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         context_dict = self.get_context_data(request=request)
         return render(request, self.template_name, context_dict)
   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
