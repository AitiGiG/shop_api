from .send_email import send_confirmation_email, send_spam
from celery import shared_task
from config.celery import app

@shared_task
# @app.task
def send_confirm_email_task(email, code):
    send_confirmation_email(email, code)

@shared_task
def send_spam_task():
    send_spam()

# shared_task | app.task