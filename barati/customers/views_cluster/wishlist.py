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
         
         user_id = m.Users.objects.get(username= request.user.username).id
         #Get tax percentages 
         super(Wishlist, self).get_each_tax()
         self.grand_total = super(Wishlist, self).calculate_grand_total(user_id)
         
         context_dict.update({'product_type_dict' : self.product_type_dict})#Used for dynamically preparing URL in the template
         context_dict.update({\
         'tax_venue' : self.tax_venue, 'tax_beautician' : self.tax_beautician, 'tax_gift' : self.tax_gift,\
         'tax_music' : self.tax_music, 'tax_photo_video' : self.tax_photo_video, 'tax_bakery' : self.tax_bakery,\
         'tax_ghodi_bagghi' : self.tax_ghodi_bagghi, 'tax_band' : self.tax_band, 'tax_mehendi' : self.tax_mehendi,\
         'tax_firework' : self.tax_firework, 'tax_card' : self.tax_card
         })
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
