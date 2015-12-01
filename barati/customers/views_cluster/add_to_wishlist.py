from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json

class Add_To_Wishlist(View):
   try:
      def __init__(self):
         self.template_name = ''
         
      def post(self, request, **kwargs):
         user = m.Users.objects.get(username=request.user.username)
         ref_id = request.POST.get('ref_id')
         message = ref_id
         wishlist = m.Wishlist(ref_id=ref_id, user_id=user.id)
         wishlist.save()
         message = "success_add_to_wish_list"
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
