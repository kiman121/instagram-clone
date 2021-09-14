from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    #  Creating message subject and sender
    subject = 'Welcome to the MoringaTribune NewsLetter'
    sender = 'mwango2047@gmail.com'

    #  Passing in the context variables
    text_content = render_to_string('email/welcome-email.txt', {'name':name})
    html_content = render_to_string('email/welcome-email.html', {'name':name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()