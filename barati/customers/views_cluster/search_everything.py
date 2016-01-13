from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from haystack.query import SearchQuerySet
from customers import models as m
import sys, json, itertools
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
         actor_auto = []
         if request.GET.get('product_type') == 'cards':
            actor_auto = SearchQuerySet().autocomplete(name_card__startswith=request.GET.get('search_everything'))[:5]#.autocomplete(actor_auto=request.GET.get('main_preference_sublocation', ''))[:5]
         if request.GET.get('product_type') == 'beauticians':
            actor_auto = SearchQuerySet().autocomplete(name_beautician__startswith=request.GET.get('search_everything'))[:5]
         if request.GET.get('product_type') == 'venues':
            actor_auto = SearchQuerySet().autocomplete(name_venue__startswith=request.GET.get('search_everything'))[:5]
         if request.GET.get('product_type') == 'all':
            actor_auto = itertools.chain(
                           SearchQuerySet().autocomplete(name_card__startswith=request.GET.get('search_everything')),\
                           SearchQuerySet().autocomplete(name_beautician__startswith=request.GET.get('search_everything')),\
                           SearchQuerySet().autocomplete(name_venue__startswith=request.GET.get('search_everything'))\
                           )
         
         suggestions_dict = {}
         suggestions = []
         for result in actor_auto:
            if request.GET.get('product_type') == 'cards':
               suggestions_dict['value'] = result.name_card
            if request.GET.get('product_type') == 'beauticians':
               suggestions_dict['value'] = result.name_beautician
            if request.GET.get('product_type') == 'venues':
               suggestions_dict['value'] = result.name_venue
            if request.GET.get('product_type') == 'all':
               if result.name_card:
                  suggestions_dict['value'] = result.name_card
               if result.name_beautician:
                  suggestions_dict['value'] = result.name_beautician
               if result.name_venue:
                  suggestions_dict['value'] = result.name_venue
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
