from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Sum
from customers import models as m
import sys, json
from dashboard import Dashboard

class Budget(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = 'customers/budget.html'
         self.current_cart_card_expense = 0
         self.current_cart_venue_expense = 0
         self.current_cart_beautician_expense = 0

      def get_context_data(self, **kwargs):
         context = super(Budget, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, **kwargs):
         query = "select id, name from card_types"
         self.card_subcategories = m.Card_Types.objects.raw(query)
         return self.card_subcategories
      
      def set_current_expenses(self, user_id):
         current_cart = m.Cart.objects.filter(user_id = user_id)
         if current_cart:
            card_expense = current_cart.filter(product_type='card').aggregate(expense = Sum('total_price'))
            venue_expense = current_cart.filter(product_type='venue').aggregate(expense = Sum('total_price'))
            beautician_expense = current_cart.filter(product_type='beautician').aggregate(expense = Sum('total_price'))
         if card_expense['expense']:
            self.current_cart_card_expense = card_expense['expense']
         if venue_expense['expense']:
            self.current_cart_venue_expense = venue_expense['expense']
         if beautician_expense['expense']:
            self.current_cart_beautician_expense = beautician_expense['expense']
         return
         
      def get(self, request, **kwargs):
         context_dict = self.get_context_data(request=request)
         user_id = m.Users.objects.get(username=request.user.username).id
         try:
            budget_details = m.Budget.objects.get(user_id=user_id)
         except m.Budget.DoesNotExist:
            budget_details = None
         self.set_current_expenses(user_id)
         context_dict.update({'budget_details' : budget_details,\
         'current_cart_card_expense' : self.current_cart_card_expense,\
         'current_cart_venue_expense' : self.current_cart_venue_expense,\
         'current_cart_beautician_expense' : self.current_cart_beautician_expense
         })
         return render(request, self.template_name, context_dict)

   except Exception as e:      
      print e
      print sys.exc_traceback.tb_lineno
