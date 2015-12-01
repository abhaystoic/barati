from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
from wishlist import Wishlist
import sys, json

class Remove_From_Wishlist(Wishlist, View):
   try:
      def __init__(self):
         self.template_name = 'customers/wishlist.html'
         self.wishlist_list = []
      
      def get_context_data(self, **kwargs):
         context = super(Remove_From_Wishlist, self).get_context_data(**kwargs)
         return context
         
      def post(self, request, **kwargs):
         ref_id = kwargs['ref_id']
         wishlist_prod_to_delete = m.Wishlist.objects.get(ref_id=ref_id)
         wishlist_prod_to_delete.delete()
         message = "success_remove_from_wishlist"
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
