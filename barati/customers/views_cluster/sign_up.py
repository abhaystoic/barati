from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from customers import models as m
import sys, json
from dashboard import Dashboard

class Sign_Up(Dashboard, View):
   try:
      def __init__(self):
         self.template_name = ''

      def get_context_data(self, **kwargs):
         context = super(Sign_Up, self).get_context_data(**kwargs)
         return context

      def get_queryset(self, *args, **kwargs):
         request = args[0]
         name = request.POST.get('name')
         email = request.POST.get('email')
         password = str(request.POST.get('password'))
         confirm_password = str(request.POST.get('confirm_password'))
         if password != confirm_password:
            message = "Passwords don't match! Try again."
         user_check_django = User.objects.filter(email=email)
         user_check_db = m.Users.objects.filter(email=email)
         if user_check_django or user_check_db:
            message = "User with that email already exists!"
            return message
         user = User.objects.create_user(email, email, password)
         user.first_name = name.split(' ')[0]
         user.save()
         #new_usr = m.Users(username=email, first_name=name, email=email)
         #new_usr.save()
         message = "success_sign_up"
         return message

      def post(self, request, **kwargs):
         message = self.get_queryset(request)
         return HttpResponse(json.dumps(message))

   except Exception as general_exception:
      print general_exception
      print sys.exc_traceback.tb_lineno
