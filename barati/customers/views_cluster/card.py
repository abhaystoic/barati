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
class Card(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/card.html'
         self.wishlist_list = []

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
         
      def get_cards(self, **kwargs):
         type = self.kwargs['type']
         query = "select id, name from cards where type_id = " + type
         self.cards = m.Cards.objects.filter(type_id=type)#raw(query)
         return self.cards

      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['card_types']
         cards = self.get_cards()
         wishlist_list = self.prepare_wishlist_data(request)
         context_dict = {'subcategories' : subcategories, 'cards' : cards, 'category' : 'card', 'wishlist_list' : wishlist_list}
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)   

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
