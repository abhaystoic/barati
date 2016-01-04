from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json, datetime

class Save_Main_Preferences(View):
   try:
      def __init__(self):
         #self.template_name = ''
         pass
      
      def get_context_data(self, **kwargs):
         context = {}
         return context

      def change_date_format_for_db(self, unformatted_date):
         formatted_date = None
         if unformatted_date:
            formatted_date = datetime.datetime.strptime(unformatted_date, '%d-%b-%Y').strftime('%Y-%m-%d')
         return formatted_date

      def post(self, request, **kwargs):
         user_id = m.Users.objects.get(username= request.user.username).id
         date = self.change_date_format_for_db(request.POST.get('main_preference_date'))
         location = request.POST.get('main_preference_location')
         sublocation = request.POST.get('main_preference_sublocation')
         
         main_preferences = m.Main_Preferences.objects.update_or_create( \
            #Filter on the basis of the user_id
            user_id=user_id, \
            #Create a new entry if new values or update if updated values
            defaults={'date':date, 'location':location, 'sublocation':sublocation}, \
            )
         message = "success_main_preferences_saved"
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
