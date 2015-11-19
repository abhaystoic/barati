#Ignore pylint whitespace warning
# pylint: disable=W0311

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
import sys


#@login_required(login_url='/auth/login/')
class dashboard(View):
   try:
      template_name = 'vendors/dashboard.html'
      
      #@method_decorator(login_required(login_url='/auth/login/'))
      def get(self, request): 
         context_dict = {}
         return render(request, self.template_name, context_dict)
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno

