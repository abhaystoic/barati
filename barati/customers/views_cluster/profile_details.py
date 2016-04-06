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
#from customers.forms import ProfileForm
from customers.forms import AddressForm

class Profile_Details(Dashboard, View):
    
    def __init__(self):
        self.template_name = 'customers/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile_Details, self).get_context_data(**kwargs)
        return context
      
      
         
    def get_user_details(self,request, **kwargs):
        
        self.user_details = m.Users.objects.get(username=request.user.username)
        return self.user_details

    

    #@login_required(login_url='/auth/login/')
    def profile(self, request, **kwargs):
        us = self.get_user_details(request)
        if request.POST:
      
            try:
               add = m.Address.objects.get(users_id=us.id)
            except m.Address.DoesNotExist:
               add=None
            form = ProfileForm(request.POST or None,instance=us)
            if not add:
               form1 = AddressForm(data=request.POST,prefix="a",instance=add)
            else:
               form1 = AddressForm(data=request.POST,prefix="a",instance=add)
            a_valid = form.is_valid()
            b_valid = form1.is_valid()
          
            if a_valid and b_valid:
           
                a = form.save()
                b = form1.save(commit=False)
             
                b.save()
                us_add = m.Address.objects.get(id=b.id)
                us_add.users_id = us.id
                us_add.save(update_fields=['users_id'])
      
        else:
            form = ProfileForm()
            form1 = AddressForm()
        return render(request,self.template_name, {'form': form,'form1':form1,'user':us})

	
        