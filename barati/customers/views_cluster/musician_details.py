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
class Musician_Details(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/musician_details.html'

      def get_context_data(self, **kwargs):
         context = super(Musician_Details, self).get_context_data(**kwargs)
         return context
      
      def get_queryset(self, **kwargs):
         query = "select id, name from music_types"
         self.musician_subcategories = m.Music_Types.objects.raw(query)
         return self.musician_subcategories
         
      def get_musician_details(self, **kwargs):
         query = "select id, name from music where id = " + str(self.kwargs['music_id'])
         self.musician_details = m.Music.objects.raw(query)
         return self.musician_details
      
      def get_user_review(self, *args, **kwargs):
         try:
            review=None
            request = args[0]
            if request.user.username:
               user_id = m.Users.objects.get(username=request.user.username).id
               ref_id = m.Music.objects.get(id=self.kwargs['music_id']).ref_id
               review = m.Reviews.objects.get(ref_id=ref_id, user_id=user_id)
               if not review:
                  review = None
         except ObjectDoesNotExist as not_reviewed_ever_exception:
            review = None   
         return review
      
      def get_all_reviews(self, **kwargs):
         reviews = None
         ref_id = m.Music.objects.get(id=self.kwargs['music_id']).ref_id
         all_reviews = m.Reviews.objects.filter(ref_id=ref_id)
         if not all_reviews:
            all_reviews = None   
         return all_reviews
      
      #@login_required(login_url='/auth/login/')
      def get(self, request, **kwargs):
         subcategories = self.get_context_data()['music_types']
         musician_details = self.get_musician_details()
         #Get tax
         tax = super(Musician_Details, self).get_tax('music')
         context_dict = {'subcategories' : subcategories, 'musician_details' : musician_details, 'tax' : tax}
         context_dict.update({'user_review' : self.get_user_review(request)})
         context_dict.update({'all_reviews' : self.get_all_reviews()})
         context_dict.update(self.get_context_data(request=request))
         return render(request, self.template_name, context_dict)

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
