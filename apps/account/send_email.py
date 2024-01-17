from django.core.mail import send_mail
from django.utils.html import format_html

def send_confirmation_email(email, code):
    activation_url = f'http://localhost:8000/account/activate/?u={code}'
    message = format_html(
        'Здравствуте, активируйте ваш аккаунт!'
        'Что бы активировать аккаунт, перейдите по ссылке'
        '<br>'
        '<a href="{}">{}</a>'
        '<br>'
        'Не передавайте этот код никому',
        activation_url, activation_url
    )

    send_mail(
        'Здравствуте, активируйте ваш аккаунт!',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False
    )
