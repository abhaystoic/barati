from django.conf import settings
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib


def mail_send(reciever,subject,body):
    fromaddr = settings.EMAIL_HOST_USER
    toaddr = [reciever, 'abhaygupta@barati.in']
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddr)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL(settings.EMAIL_HOST)
    server.login(fromaddr, settings.EMIAL_HOST_PASSWORD)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
