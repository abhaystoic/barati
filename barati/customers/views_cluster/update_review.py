from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json


class Update_Review(View):
   try:
      def __init__(self):
         self.template_name = ''
         
      def post(self, request, **kwargs):
         try:
            user = m.Users.objects.get(username=request.user.username)
            ref_id = request.POST.get('update_reviewed_ref_id')
            review=m.Reviews.objects.get(user_id=user.id,ref_id=ref_id)
            review.title = request.POST.get('update_title_review')
            review.detailed_review = request.POST.get('update_detailed_review')
            review.recommended = request.POST.get('update_recommendation') 
            review.save(update_fields=['title', 'detailed_review','recommended'])
            message="success_update_review"
         except Exception as general_exception:
            message = str(general_exception)
            print general_exception
            print sys.exc_traceback.tb_lineno
         return HttpResponse(json.dumps(message))
         

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno