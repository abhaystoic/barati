from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard

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
         query = "select id, name from beauticians where type_id = " + type + " and gender = '" + str(gender) + "'"
         if gender == None:
            self.beauticians = m.Beauticians.objects.filter(type_id=type, actual_price__range=self.popular_price_filter_values)#raw(query)
         else:
            self.beauticians = m.Beauticians.objects.filter(\
               type_id=type, gender=str(gender),\
               actual_price__range=self.popular_price_filter_values)# use raw query
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
         context_dict = {
            'subcategories' : subcategories, 'beauticians' : beauticians, 'category' : 'beauticians', 'type' : self.kwargs['type'], \
            'wishlist_list' : wishlist_list, 'filter_values' : filter_values,\
            'popular_price_filter_values' : self.popular_price_filter_values
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
      
      def post(self, request, **kwargs):
         slider_values = request.POST.get('slider');
         selected_filter_values = None
         if slider_values is not None:
            selected_filter_values = tuple(slider_values.split(','))
         subcategories = self.get_context_data()['beautician_types']
         beauticians = self.get_price_filtered_beauticians(request, selected_filter_values)
         wishlist_list = self.prepare_wishlist_data(request)
         context_dict = {
            'subcategories' : subcategories, 'beauticians' : beauticians, 'category' : 'beauticians', 'type' : self.kwargs['type'],\
            'wishlist_list' : wishlist_list, 'filter_values' : self.filter_values,\
            'selected_filter_values' : selected_filter_values
            }
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)
         
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
