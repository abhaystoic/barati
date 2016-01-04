from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from haystack.query import SearchQuerySet
from customers import models as m
import sys, json
from dashboard import Dashboard

class Search_Everything(Dashboard, View):
   try:
      def __init__(self):
         pass
      
      def get_type(self, type_name):
         
         card_types = m.Card_Types.objects.filter(name=type_name)
         if card_types:
            return 'card'
         
         beautician_types = m.Beautician_Types.objects.filter(name=type_name)
         if beautician_types:
            return 'beautician'
         
         return None   
              
      def get(self, request, **kwargs):
         '''
         Used for suggesting locality based on sublocation search string
         Please refer http://blog.appliedinformaticsinc.com/autocomplete-quick-intro-django-haystack-solr-jquery/
         '''
         actor_auto= SearchQuerySet().autocomplete(name__startswith=request.GET.get('search_everything' ))[:5]#.autocomplete(actor_auto=request.GET.get('main_preference_sublocation', ''))[:5]
         suggestions_dict = {}
         suggestions = []
         for result in actor_auto:
            suggestions_dict['value'] = result.name
            suggestions_dict['id'] = (result.id).split('.')[2]
            suggestions_dict['type'] = self.get_type(result.type)
            suggestions.append(suggestions_dict)
            suggestions_dict = {}
         data = json.dumps({
               'results': suggestions
            })
         return HttpResponse(data, content_type='application/json')

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
