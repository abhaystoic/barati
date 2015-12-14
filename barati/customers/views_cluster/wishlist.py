from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
from dashboard import Dashboard
import sys, json

class Wishlist(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/wishlist.html'
         self.wishlist_list = []
         self.product_type_dict = {}
      
      def get_context_data(self, **kwargs):
         context = super(Wishlist, self).get_context_data(**kwargs)
         return context
      
      def prepare_wishlist(self, *args, **kwargs):
         request = args[0]
         if request.user.username:
            user_id = m.Users.objects.get(username= request.user.username).id
            query = "select id, ref_id from wishlist where user_id=" + str(user_id)
            wishlist = m.Wishlist.objects.raw(query)
            for wish in wishlist:
            
               cards_in_wishlist = m.Cards.objects.filter(ref_id=wish.ref_id)
               if cards_in_wishlist:
                  self.wishlist_list.append(cards_in_wishlist[0])
                  self.product_type_dict.update({wish.ref_id : 'card'})
                  
               beauticians_in_wishlist = m.Beauticians.objects.filter(ref_id=wish.ref_id)
               if beauticians_in_wishlist:
                  self.wishlist_list.append(beauticians_in_wishlist[0])
                  self.product_type_dict.update({wish.ref_id : 'beautician'})
                  
         return self.wishlist_list
         
      def get(self, request, **kwargs):
         wishlist_list = self.prepare_wishlist(request)
         context_dict = {'wishlist_list' : wishlist_list}
         context_dict.update({'product_type_dict' : self.product_type_dict})#Used for dynamically preparing URL in the template
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
