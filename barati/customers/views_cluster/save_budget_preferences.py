from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json

class Save_Budget_Preferences(View):
   try:
      def __init__(self):
         #self.template_name = ''
         pass
      
      def get_context_data(self, **kwargs):
         context = {}
         return context
      
      def float_typecast(self, ele):
         print "ele='", str(ele).strip(), "'"
         if ele is not None or str(ele).strip() != '':
            return float(ele)
         else:
            return None
         
      def post(self, request, **kwargs):
         user_id = m.Users.objects.get(username= request.user.username).id
         print "rec = '", request.POST.get('min_master'), "'"
         min_master = self.float_typecast(request.POST.get('min_master'))
         max_master = self.float_typecast(request.POST.get('max_master'))
         min_venue = self.float_typecast(request.POST.get('min_venue'))
         max_venue = self.float_typecast(request.POST.get('max_venue'))
         min_card = self.float_typecast(request.POST.get('min_card'))
         max_card = self.float_typecast(request.POST.get('max_card'))
         min_beautician = self.float_typecast(request.POST.get('min_beautician'))
         max_beautician = self.float_typecast(request.POST.get('max_beautician'))
         min_mehendi = self.float_typecast(request.POST.get('min_mehendi'))
         max_mehendi = self.float_typecast(request.POST.get('max_mehendi'))
         min_music = self.float_typecast(request.POST.get('min_music'))
         max_music = self.float_typecast(request.POST.get('max_music'))
         min_gift = self.float_typecast(request.POST.get('min_gift'))
         max_gift = self.float_typecast(request.POST.get('max_gift'))
         min_tent = self.float_typecast(request.POST.get('min_tent'))
         max_tent = self.float_typecast(request.POST.get('max_tent'))
         
         budget = m.Budget.objects.update_or_create( \
            min_master=min_master, max_master=max_master, min_venue=min_venue, max_venue=max_venue,\
            min_card=min_card, max_card=max_card, min_beautician=min_beautician, max_beautician=max_beautician,\
            min_mehendi=min_mehendi, max_mehendi=max_mehendi, min_music=min_music, max_music=max_music,\
            min_gift=min_gift, max_gift=max_gift, min_tent=min_tent, max_tent=max_tent, \
            user_id=user_id\
            )
         budget.save()
         message = "success_budget_preferences_saved"
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
