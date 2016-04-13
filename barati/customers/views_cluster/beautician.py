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
from el_pagination.decorators import page_template

#@login_required(login_url='/auth/login/')
class Beautician(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/beautician.html'
         self.wishlist_list = []
         self.filter_values = (0, 10000)
         self.popular_price_filter_values = (2000, 7000)

      def get_context_data(self, **kwargs):
         context = super(Beautician, self).get_context_data(**kwargs)   
         return context

      def get_queryset(self, **kwargs):
         query = "select id, name from beautician_types"
         self.beautician_subcategories = m.Beautician_Types.objects.raw(query)
         return self.beautician_subcategories
      
      def prepare_wishlist_data(self, *args, **kwargs):
         request = args[0]
         if request.user.username:
            user_id = m.Users.objects.get(username= request.user.username).id
            query = "select id, ref_id from wishlist where user_id=" + str(user_id)
            wishlist = m.Wishlist.objects.raw(query)
            for wish in wishlist:
               self.wishlist_list.append(str(wish.ref_id))
         return self.wishlist_list   
         
      def get_beauticians(self, request, **kwargs):
         type = self.kwargs['type']
         gender = request.GET.get('for')
         home_visit = request.GET.get('home_visit')
         confidence_check_filter = request.GET.get('confidence_check_filter')
         #query = "select id, name from beauticians where type_id = " + type + " and gender = '" + str(gender) + "'"
         
         #Filter by gender
         if gender == None or gender == 'all':
            self.beauticians = m.Beauticians.objects.filter(type_id=type, actual_price__range=self.popular_price_filter_values)#raw(query)
         else:
            self.beauticians = m.Beauticians.objects.filter(\
               type_id=type, gender=str(gender),\
               actual_price__range=self.popular_price_filter_values)# use raw query

         #filter product according to availability
         if request.user.username:
            user_id = m.Users.objects.get(username= request.user.username).id
            try:
               preference_date=m.Main_Preferences.objects.get(user_id=user_id).date
            except m.Main_Preferences.DoesNotExist:
               preference_date=None
            if preference_date:
               try:
                  beaut_booked=m.Product_Availability.objects.get(date=preference_date , ref_id__startswith='BTN')
                  self.venues=self.beauticians.exclude(ref_id=beaut_booked.ref_id)
               except m.Product_Availability.DoesNotExist:
                  beaut_booked=None
         
         #Filter by home visit availability
         if home_visit == 'available':
            self.beauticians = self.beauticians.exclude(home_visit_charge__isnull=True)
            self.beauticians = self.beauticians.exclude(home_visit_charge=0)

         #Filter by barati confidence. Select only if confidence > 20%
         if confidence_check_filter == 'add_confidence':
            self.beauticians = self.beauticians.exclude(barati_confidence_perc__isnull=True)
            self.beauticians = self.beauticians.exclude(barati_confidence_perc__lte=20.0)

         #Filter by discount
         discounts_dict = {}
         discounts_dict = { 
            '0-10' : request.GET.get('0-10'),
            '10-20' : request.GET.get('10-20'), 
            '20-30' : request.GET.get('20-30'),
            '30-40' : request.GET.get('30-40'),
            '40-100' : request.GET.get('40-100'),
         }
         
         beauticians, beauticians_0_10, beauticians_10_20, beauticians_20_30, beauticians_30_40, beauticians_40_100 = [], [], [], [], [], []
         for key, value in discounts_dict.iteritems():
            if value == 'filter':
               if key == '0-10':
                  if self.beauticians:
                     #self.beauticians = self.beauticians.exclude(discount_perc__isnull=True)
                     beauticians_0_10 = self.beauticians.filter(discount_perc__range=(0,10))
               if key == '10-20':
                  if self.beauticians:
                     #self.beauticians = self.beauticians.exclude(discount_perc__isnull=True)
                     beauticians_10_20 = self.beauticians.filter(discount_perc__range=(10,20))
               if key == '20-30':
                  if self.beauticians:
                     #self.beauticians = self.beauticians.exclude(discount_perc__isnull=True)
                     beauticians_20_30 = self.beauticians.filter(discount_perc__range=(20,30))
               if key == '30-40':
                  if self.beauticians:
                     #self.beauticians = self.beauticians.exclude(discount_perc__isnull=True)
                     beauticians_30_40 = self.beauticians.filter(discount_perc__range=(30,40))
               if key == '40-100':
                  if self.beauticians:
                     #self.beauticians = self.beauticians.exclude(discount_perc__isnull=True)
                     beauticians_40_100 = self.beauticians.filter(discount_perc__range=(40,100))
         
         for key, value in discounts_dict.iteritems():
            if value == 'filter':
               self.beauticians = None
         beauticians =  list(chain(beauticians_0_10, beauticians_10_20, beauticians_20_30, beauticians_30_40, beauticians_40_100))
         if beauticians:
            self.beauticians = beauticians
         if self.beauticians is None:
            self.beauticians = []
         return self.beauticians
      
      def get_price_filtered_beauticians(self, request, selected_filter_values, **kwargs):
         type = self.kwargs['type']
         gender = request.GET.get('for')
         query = "select id, name from beauticians where type_id = " + type + " and gender = '" + str(gender) + "'"
         if gender == None:
            self.beauticians = m.Beauticians.objects.filter(type_id=type, actual_price__range=selected_filter_values)#raw(query)
         else:
            self.beauticians = m.Beauticians.objects.filter(\
               type_id=type, gender=str(gender),\
               actual_price__range=selected_filter_values)# use raw query
         return self.beauticians
      
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['beautician_types']
         beauticians = self.get_beauticians(request)
         wishlist_list = self.prepare_wishlist_data(request)
         filter_values = self.filter_values
         #Get tax 
         tax = super(Beautician, self).get_tax('beautician')
         context_dict = {
            'subcategories' : subcategories, 'beauticians' : beauticians, 'category' : 'beauticians', 'type' : self.kwargs['type'], \
            'wishlist_list' : wishlist_list, 'filter_values' : filter_values, \
            'popular_price_filter_values' : self.popular_price_filter_values, 'tax' : tax
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
      
      @page_template('customers/beautician.html')
      def post(self, request, **kwargs):
         slider_values = request.POST.get('slider');
         selected_filter_values = None
         if slider_values is not None:
            selected_filter_values = tuple(slider_values.split(','))
         subcategories = self.get_context_data()['beautician_types']
         beauticians = self.get_price_filtered_beauticians(request, selected_filter_values)
         wishlist_list = self.prepare_wishlist_data(request)
         #Get tax 
         tax = super(Beautician, self).get_tax('beautician')
         context_dict = {
            'subcategories' : subcategories, 'beauticians' : beauticians, 'category' : 'beauticians', 'type' : self.kwargs['type'],\
            'wishlist_list' : wishlist_list, 'filter_values' : self.filter_values,\
            'selected_filter_values' : selected_filter_values, 'tax' : tax
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
         
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
