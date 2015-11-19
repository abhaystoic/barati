from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
import sys

#@login_required(login_url='/auth/login/')
class dashboard(View):
   try:
      template_name = 'customers/index.html'
      
      #@method_decorator(login_required(login_url='/auth/login/'))
      def get(self, request): 
         context_dict = {}
         return render(request, self.template_name, context_dict)
   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno

#@login_required(login_url='/auth/login/')
def venue(request, type):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/venue.html', context_dict, context_instance=context)

   
#@login_required(login_url='/auth/login/')
def product_details(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/product_details.html', context_dict, context_instance=context)

#@login_required(login_url='/auth/login/')
def blog(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/blog.html', context_dict, context_instance=context)
   
#@login_required(login_url='/auth/login/')
def cart(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/cart.html', context_dict, context_instance=context)   

#@login_required(login_url='/auth/login/')
def checkout(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/checkout.html', context_dict, context_instance=context)         
   
#@login_required(login_url='/auth/login/')
def shop(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/shop.html', context_dict, context_instance=context)   
   
#@login_required(login_url='/auth/login/')
def contact_us(request):
   context = RequestContext(request)
   context_dict = {}
   return render_to_response('customers/contact_us.html', context_dict, context_instance=context)   
