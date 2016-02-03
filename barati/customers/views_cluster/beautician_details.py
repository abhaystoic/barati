from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from customers import models as m
import sys, json
from dashboard import Dashboard

#@login_required(login_url='/auth/login/')
class Beautician_Details(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/beautician_details.html'

      def get_context_data(self, **kwargs):
         context = super(Beautician_Details, self).get_context_data(**kwargs)
         return context
      
      def get_queryset(self, **kwargs):
         query = "select id, name from beautician_types"
         self.beautician_subcategories = m.Beautician_Types.objects.raw(query)
         return self.beautician_subcategories
         
      def get_beautician_details(self, **kwargs):
         query = "select id, name from beauticians where id = " + str(self.kwargs['beautician_id'])
         self.beautician_details = m.Beauticians.objects.raw(query)
         return self.beautician_details
      
      def get_user_review(self, *args, **kwargs):
         try:
            review=None
            request = args[0]
            if request.user.username:
               user_id = m.Users.objects.get(username=request.user.username).id
               ref_id = m.Beauticians.objects.get(id=self.kwargs['beautician_id']).ref_id
               review = m.Reviews.objects.get(ref_id=ref_id, user_id=user_id)
               if not review:
                  review = None
         except ObjectDoesNotExist as not_reviewed_ever_exception:
            review = None   
         return review
      
      def get_all_reviews(self, **kwargs):
         reviews = None
         ref_id = m.Beauticians.objects.get(id=self.kwargs['beautician_id']).ref_id
         all_reviews = m.Reviews.objects.filter(ref_id=ref_id)
         if not all_reviews:
            all_reviews = None   
         return all_reviews
      
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['beautician_types']
         beautician_details = self.get_beautician_details()
         #Get tax
         tax = super(Beautician_Details, self).get_tax('beautician')
         context_dict = {'subcategories' : subcategories, 'beautician_details' : beautician_details, 'tax' : tax}
         context_dict.update({'user_review' : self.get_user_review(request)})
         context_dict.update({'all_reviews' : self.get_all_reviews()})
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
