from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from itertools import chain
from dashboard import Dashboard

#@login_required(login_url='/auth/login/')
class Card(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/card.html'
         self.wishlist_list = []
         self.filter_values = (0, 500)
         self.popular_price_filter_values = (20, 200)

      def get_context_data(self, **kwargs):
         context = super(Card, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs):
         query = "select id, name from card_types"
         self.card_subcategories = m.Card_Types.objects.raw(query)
         return self.card_subcategories
      
      def prepare_wishlist_data(self, *args, **kwargs):
         request = args[0]
         if request.user.username:
            user_id = m.Users.objects.get(username= request.user.username).id
            query = "select id, ref_id from wishlist where user_id=" + str(user_id)
            wishlist = m.Wishlist.objects.raw(query)
            for wish in wishlist:
               self.wishlist_list.append(str(wish.ref_id))
         return self.wishlist_list   
         
      def get_cards(self, request, **kwargs):
         type = self.kwargs['type']
         query = "select id, name from cards where type_id = " + type
         self.cards = m.Cards.objects.filter(type_id=type, actual_price__range=self.popular_price_filter_values)#raw(query)
         
         confidence_check_filter = request.GET.get('confidence_check_filter')
         #Filter by barati confidence. Select only if confidence > 20%
         if confidence_check_filter == 'add_confidence':
            self.cards = self.cards.exclude(barati_confidence_perc__isnull=True)
            self.cards = self.cards.exclude(barati_confidence_perc__lte=20.0)
            
         #Filter by discount
         discounts_dict = {}
         discounts_dict = { 
            '0-10' : request.GET.get('0-10'),
            '10-20' : request.GET.get('10-20'), 
            '20-30' : request.GET.get('20-30'),
            '30-40' : request.GET.get('30-40'),
            '40-100' : request.GET.get('40-100'),
         }
         
         cards, cards_0_10, cards_10_20, cards_20_30, cards_30_40, cards_40_100 = [], [], [], [], [], []
         for key, value in discounts_dict.iteritems():
            if value == 'filter':
               if key == '0-10':
                  if self.cards:
                     #self.cards = self.cards.exclude(discount_perc__isnull=True)
                     cards_0_10 = self.cards.filter(discount_perc__range=(0,10))
               if key == '10-20':
                  if self.cards:
                     #self.cards = self.cards.exclude(discount_perc__isnull=True)
                     cards_10_20 = self.cards.filter(discount_perc__range=(10,20))
               if key == '20-30':
                  if self.cards:
                     #self.cards = self.cards.exclude(discount_perc__isnull=True)
                     cards_20_30 = self.cards.filter(discount_perc__range=(20,30))
               if key == '30-40':
                  if self.cards:
                     #self.cards = self.cards.exclude(discount_perc__isnull=True)
                     cards_30_40 = self.cards.filter(discount_perc__range=(30,40))
               if key == '40-100':
                  if self.cards:
                     #self.cards = self.cards.exclude(discount_perc__isnull=True)
                     cards_40_100 = self.cards.filter(discount_perc__range=(40,100))
         
         for key, value in discounts_dict.iteritems():
            if value == 'filter':
               self.cards = None
         cards =  list(chain(cards_0_10, cards_10_20, cards_20_30, cards_30_40, cards_40_100))
         if cards:
            self.cards = cards
         if self.cards is None:
            self.cards = []
         return self.cards
      
      def get_filtered_cards_list(self, request, selected_filter_values, **kwargs):
         type = self.kwargs['type']
         query = "select id, name from cards where type_id = " + type + \
         " and actual_price between " + str(selected_filter_values[0]) + " and " + str(selected_filter_values[1])
         self.cards = m.Cards.objects.filter(type_id=type, actual_price__range=selected_filter_values)#change to raw(query)
         return self.cards
      
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['card_types']
         cards = self.get_cards(request)
         wishlist_list = self.prepare_wishlist_data(request)
         filter_values = self.filter_values
         
         #Get tax 
         tax = super(Card, self).get_tax('card')
         context_dict = {
            'subcategories' : subcategories, 'cards' : cards, 'category' : 'card', 'type' : self.kwargs['type'], \
            'wishlist_list' : wishlist_list, 'filter_values' : filter_values,\
            'popular_price_filter_values' : self.popular_price_filter_values, 'tax' : tax
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
      
      @page_template('customers/card.html')
      def post(self, request, **kwargs):
         slider_values = request.POST.get('slider')
         selected_filter_values = None
         if slider_values is not None:
            selected_filter_values = tuple(slider_values.split(','))
         subcategories = self.get_context_data()['card_types']
         cards = self.get_filtered_cards_list(request, selected_filter_values)
         wishlist_list = self.prepare_wishlist_data(request)
         context_dict = {
            'subcategories' : subcategories, 'cards' : cards, 'category' : 'card', 'type' : self.kwargs['type'],\
            'wishlist_list' : wishlist_list, 'filter_values' : self.filter_values,\
            'selected_filter_values' : selected_filter_values, 'tax' : tax
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
