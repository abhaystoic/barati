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

class Search(Dashboard, View):
   try:
      def __init__(self):
         #self.template_name = 'customers/beautician_details.html'
         pass

      def get(self, request, **kwargs):
         '''
         Used for suggesting locality based on sublocation search string
         Please refer http://blog.appliedinformaticsinc.com/autocomplete-quick-intro-django-haystack-solr-jquery/
         '''
         actor_auto= SearchQuerySet().autocomplete(locality__startswith=request.GET.get('main_preference_sublocation' ))[:5]#.autocomplete(actor_auto=request.GET.get('main_preference_sublocation', ''))[:5]
         suggestions = [result.locality for result in actor_auto]
         suggestions = list(set(suggestions))
         data = json.dumps({
               'results': suggestions
            })
         return HttpResponse(data, content_type='application/json')

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
