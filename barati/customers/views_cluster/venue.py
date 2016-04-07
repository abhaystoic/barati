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
class Venue(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/venue.html'
         self.wishlist_list = []
         self.filter_values = (10000, 60000)
         self.popular_price_filter_values = (18000, 40000)
         self.venues = None

      def get_context_data(self, **kwargs):
         context = super(Venue, self).get_context_data(**kwargs)   
         return context

      def get_queryset(self, **kwargs):
         query = "select id, name from venue_types"
         self.venue_subcategories = m.Venue_Types.objects.raw(query)
         return self.venue_subcategories
      
      def prepare_wishlist_data(self, *args, **kwargs):
         request = args[0]
         if request.user.username:
            user_id = m.Users.objects.get(username= request.user.username).id
            query = "select id, ref_id from wishlist where user_id=" + str(user_id)
            wishlist = m.Wishlist.objects.raw(query)
            for wish in wishlist:
               self.wishlist_list.append(str(wish.ref_id))
         return self.wishlist_list   
         
      def get_venues(self, request, **kwargs):
         
         type = self.kwargs['type']
         confidence_check_filter = request.GET.get('confidence_check_filter')
         self.venues = m.Venues.objects.filter(type_id=type)
         #Filter by barati confidence. Select only if confidence > 20%
         if confidence_check_filter == 'add_confidence':
            self.venues = self.venues.exclude(barati_confidence_perc__isnull=True)
            self.venues = self.venues.exclude(barati_confidence_perc__lte=20.0)
            #if usr logged in main_pref se data uthao n exclude venue not available

         #Filter by discount
         discounts_dict = {}
         discounts_dict = { 
            '0-10' : request.GET.get('0-10'),
            '10-20' : request.GET.get('10-20'), 
            '20-30' : request.GET.get('20-30'),
            '30-40' : request.GET.get('30-40'),
            '40-100' : request.GET.get('40-100'),
         }
         
         venues, venues_0_10, venues_10_20, venues_20_30, venues_30_40, venues_40_100 = [], [], [], [], [], []
         for key, value in discounts_dict.iteritems():
            if value == 'filter':
               if key == '0-10':
                  if self.venues:
                     #self.venues = self.venues.exclude(discount_perc__isnull=True)
                     venues_0_10 = self.venues.filter(discount_perc__range=(0,10))
               if key == '10-20':
                  if self.venues:
                     #self.venues = self.venues.exclude(discount_perc__isnull=True)
                     venues_10_20 = self.venues.filter(discount_perc__range=(10,20))
               if key == '20-30':
                  if self.venues:
                     #self.venues = self.venues.exclude(discount_perc__isnull=True)
                     venues_20_30 = self.venues.filter(discount_perc__range=(20,30))
               if key == '30-40':
                  if self.venues:
                     #self.venues = self.venues.exclude(discount_perc__isnull=True)
                     venues_30_40 = self.venues.filter(discount_perc__range=(30,40))
               if key == '40-100':
                  if self.venues:
                     #self.venues = self.venues.exclude(discount_perc__isnull=True)
                     venues_40_100 = self.venues.filter(discount_perc__range=(40,100))
         
         for key, value in discounts_dict.iteritems():
            if value == 'filter':
               self.venues = None
         venues =  list(chain(venues_0_10, venues_10_20, venues_20_30, venues_30_40, venues_40_100))
         if venues:
            self.venues = venues
         return self.venues
      
      def get_price_filtered_venues(self, request, selected_filter_values, **kwargs):
         type = self.kwargs['type']
         query = "select id, name from venues where type_id = " + type
         if selected_filter_values is not None:
            self.venues = m.Venues.objects.filter(type_id=type, actual_price__range=selected_filter_values)#raw(query)
         else:
            self.venues = m.Venues.objects.filter(type_id=type)#raw(query)
         return self.venues
      
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['venue_types']
         venues = self.get_venues(request)
         wishlist_list = self.prepare_wishlist_data(request)
         filter_values = self.filter_values
         #Get tax 
         tax = super(Venue, self).get_tax('venue')
         context_dict = {
            'subcategories' : subcategories, 'venues' : venues, 'category' : 'venues', 'type' : self.kwargs['type'], \
            'wishlist_list' : wishlist_list, 'filter_values' : filter_values, \
            'popular_price_filter_values' : self.popular_price_filter_values, 'tax' : tax
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
         
      @page_template('customers/venue.html')
      def post(self, request, **kwargs):
         slider_values = request.POST.get('slider');
         selected_filter_values = None
         if slider_values is not None:
            selected_filter_values = tuple(slider_values.split(','))
         subcategories = self.get_context_data()['venue_types']
         venues = self.get_price_filtered_venues(request, selected_filter_values)
         wishlist_list = self.prepare_wishlist_data(request)
         #Get tax 
         tax = super(Venue, self).get_tax('venue')
         context_dict = {
            'subcategories' : subcategories, 'venues' : venues, 'category' : 'venues', 'type' : self.kwargs['type'],\
            'wishlist_list' : wishlist_list, 'filter_values' : self.filter_values,\
            'selected_filter_values' : selected_filter_values, 'tax' : tax
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
         
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
