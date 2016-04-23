from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponse
from customers import models as m
import sys, json
from dashboard import Dashboard
from customers.forms import ContactUsForm


# @login_required(login_url='/auth/login/')
def Contact_Us(request):
    form = ContactUsForm()
    context = {
        'form': form,
    }
    return render(request, 'customers/contact_us.html', context)