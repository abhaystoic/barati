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
class Card_Details(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/card_details.html'

      def get_context_data(self, **kwargs):
         context = super(Card_Details, self).get_context_data(**kwargs)
         return context
      
      def get_queryset(self, **kwargs):
         query = "select id, name from card_types"
         self.card_subcategories = m.Card_Types.objects.raw(query)
         return self.card_subcategories
         
      def get_card_details(self, **kwargs):
         query = "select id, name from cards where id = " + str(self.kwargs['card_id'])
         self.card_details = m.Cards.objects.raw(query)
         return self.card_details

      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['card_types']
         card_details = self.get_card_details()
         context_dict = {'subcategories' : subcategories, 'card_details' : card_details}
         context_dict.update(self.get_context_data())
         
         return render(request, self.template_name, context_dict)   

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno