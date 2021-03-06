from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from customers import models as m
import sys, json
from dashboard import Dashboard

#@login_required(login_url='/auth/login/')
class Card_Details(Dashboard, View):
   try:
      def __init__(self):
         self.wishlist_list = []
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
      
      def prepare_wishlist_data(self, *args, **kwargs):
         request = args[0]
         if request.user.username:
            user_id = m.Users.objects.get(username= request.user.username).id
            query = "select id, ref_id from wishlist where user_id=" + str(user_id)
            wishlist = m.Wishlist.objects.raw(query)
            for wish in wishlist:
               self.wishlist_list.append(str(wish.ref_id))
         return self.wishlist_list    
      
      def get_card_colors(self, **kwargs):
         card_colors = m.Card_Colors.objects.filter(card_id=self.kwargs['card_id'])
         return card_colors
      
      def get_user_review(self, *args, **kwargs):
         try:
            review=None
            request = args[0]
            if request.user.username:
               user_id = m.Users.objects.get(username=request.user.username).id
               ref_id = m.Cards.objects.get(id=self.kwargs['card_id']).ref_id
               review = m.Reviews.objects.get(ref_id=ref_id, user_id=user_id)
               if not review:
                  review = None
         except ObjectDoesNotExist as not_reviewed_ever_exception:
            review = None   
         return review
      
      def get_all_reviews(self, **kwargs):
         reviews = None
         ref_id = m.Cards.objects.get(id=self.kwargs['card_id']).ref_id
         all_reviews = m.Reviews.objects.filter(ref_id=ref_id)
         if not all_reviews:
            all_reviews = None   
         return all_reviews
      
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['card_types']
         card_details = self.get_card_details()
         wishlist_list = self.prepare_wishlist_data(request)
         #Get tax 
         tax = super(Card_Details, self).get_tax('card')
         context_dict = {'subcategories' : subcategories, 'card_details' : card_details, 'wishlist_list' : wishlist_list,\
         'tax' : tax
         }
         context_dict.update({'user_review' : self.get_user_review(request)})
         context_dict.update({'all_reviews' : self.get_all_reviews()})
         context_dict.update({'card_colors' : self.get_card_colors()})
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)   

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
