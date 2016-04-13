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
from customers.forms import ProfileForm,AddressForm,ReligionForm

class Profile(Dashboard, View):
    
    def __init__(self):
        self.template_name = 'customers/profile.html'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        return context
      
      
         
    def dispatch(self,request,*args, **kwargs):
        
        self.us = m.Users.objects.get(username=request.user.username)
        try:  
            self.add = m.Address.objects.get(users_id=self.us.id)
        except m.Address.DoesNotExist:
            self.add=None
        try:
            self.rel = m.Religion.objects.get(users_id=self.us.id)
        except m.Religion.DoesNotExist:
            self.rel=None
        return super(Profile, self).dispatch(request, *args, **kwargs)

    

    #@login_required(login_url='/auth/login/')
    def get(self, request, **kwargs):
        form = ProfileForm(instance=self.us)
        form1 = AddressForm(prefix="a",instance=self.add)
        form2=ReligionForm(prefix="b",instance=self.rel)
            
        return render(request, 'customers/profile.html', {'form': form,'form1':form1,'form2':form2})
    def post(self, request, **kwargs):
        
        form = ProfileForm(request.POST or None,instance=self.us)
        form1 = AddressForm(data=request.POST,prefix="a",instance=self.add)
        form2=ReligionForm(data=request.POST,prefix="b",instance=self.rel)
        a_valid = form.is_valid()
        b_valid = form1.is_valid()
        c_valid = form2.is_valid()
        
        if a_valid and b_valid and c_valid:

            return self.form_valid(request,form,form1, form2)
        else:
            return self.get(request)

           
    def form_valid(self,request, form,form1, form2):

        a = form.save()
        b = form1.save(commit=False)
        c = form2.save(commit=False)
        b.save()
        c.save()
        us_add = m.Address.objects.get(id=b.id)
        us_add.users_id = self.us.id
        us_add.save(update_fields=['users_id'])
        us_rel = m.Religion.objects.get(id=c.id)
        us_rel.users_id =self.us.id
        us_rel.save(update_fields=['users_id'])
        return render(request, self.template_name, {'form': form,'form1':form1,'form2':form2})
