import json
from customers.mail import mail_send
from django.http import HttpResponse

def Contact_Us_Submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        body = 'Name : ' + name + '\nEmail : ' + email + '\n' + text
        mail_send('contactus@barati.in', 'Mail from portal : Contact Us enquiry', body)
        return HttpResponse(
            json.dumps([]),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )