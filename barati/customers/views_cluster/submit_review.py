from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json

class Submit_Review(View):
   try:
      def __init__(self):
         self.template_name = ''
         
      def post(self, request, **kwargs):
         try:
            user = m.Users.objects.get(username=request.user.username)
            ref_id = request.POST.get('reviewed_ref_id')
            title_review = request.POST.get('title_review')
            detailed_review = request.POST.get('detailed_review')
            recommendation = request.POST.get('recommendation') 
            review = m.Reviews(user=user, ref_id=ref_id, title=title_review, detailed_review=detailed_review,recommended=recommendation)
            review.save()
            message="success_submit_review"
         except Exception as general_exception:
            message = str(general_exception)
            print general_exception
            print sys.exc_traceback.tb_lineno
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
