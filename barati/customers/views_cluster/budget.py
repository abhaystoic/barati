from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard

class Budget(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/budget.html'

      def get_context_data(self, **kwargs):
         context = super(Budget, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs):
         query = "select id, name from card_types"
         self.card_subcategories = m.Card_Types.objects.raw(query)
         return self.card_subcategories

      def get(self, request, **kwargs):
         context_dict = self.get_context_data(request=request)
         user_id = m.Users.objects.get(username=request.user.username).id
         budget_details = m.Budget.objects.get(user_id=user_id)
         context_dict.update({'budget_details' : budget_details})
         return render(request, self.template_name, context_dict)

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
