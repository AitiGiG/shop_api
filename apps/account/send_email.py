from django.core.mail import send_mail
from django.utils.html import format_html

def send_confirmation_email(email, code):
    activation_url = f'http://localhost:8000/account/activate/?u={code}'
    message = format_html(
<<<<<<< HEAD
        'Здравствуйте, активируйте ваш аккаунт'
        'Чтобы активировать аккаунт, перейдите по ссылке'
        '<br>'
        '<a href= "{}"></a>'
        '<br>'
        'Не передовайте код никому',
=======
        'Здравствуте, активируйте ваш аккаунт!'
        'Что бы активировать аккаунт, перейдите по ссылке'
        '<br>'
        '<a href="{}">{}</a>'
        '<br>'
        'Не передавайте этот код никому',
>>>>>>> 6fad788c6525e51f3adca4d67d93c9051ec87410
        activation_url, activation_url
    )

    send_mail(
<<<<<<< HEAD
        'Здравствуйте',
=======
        'Здравствуте, активируйте ваш аккаунт!',
>>>>>>> 6fad788c6525e51f3adca4d67d93c9051ec87410
        message,
        'test@gmail.com',
        [email],
        fail_silently=False
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 6fad788c6525e51f3adca4d67d93c9051ec87410
