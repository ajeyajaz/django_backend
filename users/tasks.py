from  celery import  shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def  send_welcome_email(username, email):
    subject = 'Welcome to MyApp!'
    message = f'Hello {username},\nThanks for registering on MyApp.'
    send_mail(subject, message ,settings.DEFAULT_FROM_EMAIL, [email])
