from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard
#@login_required(login_url='/auth/login/')
class Venue(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/venue.html'

      def get_context_data(self, **kwargs):
         context = super(Venue, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs): 
         #type = self.kwargs['type']
         query = "select id, name from venue_types"
         self.venue_subcategories = m.Venue_Types.objects.raw(query)
         return self.venue_subcategories
         
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         print self.get_context_data()
         subcategories = self.get_context_data()['venue_types']
         context_dict = {'subcategories' : subcategories}
         context_dict.update(self.get_context_data())
         return render(request, self.template_name, context_dict)   
      
      '''
      Save something back to DB
       def get_object(self):
          # Call the superclass
          object = super(AuthorDetailView, self).get_object()
          # Record the last accessed date
          object.last_accessed = timezone.now()
          object.save()
          # Return the object
          return object
      '''
      
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
