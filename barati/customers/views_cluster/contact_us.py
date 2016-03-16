from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard
from customers.forms import ContactUsForm
from customers.mail import mail_send

# @login_required(login_url='/auth/login/')
def Contact_Us(request):
    form = ContactUsForm(request.POST or None)
    mailSuccess = 0
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        text = form.cleaned_data['text']
        body = 'Name : ' + name + '\nEmail : ' + email + '\n' + text
        mail_send('contactus@barati.in', 'New Contact Us Info', body)
        mailSuccess = 1

    form = ContactUsForm()
    context = {
        'form': form,
        'mailSuccess': mailSuccess
    }
    return render(request, 'customers/contact_us.html', context)