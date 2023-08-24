import random

from config import settings
from users.models import User

from django.core.mail import send_mail


# def get_random_password():
#     pas = ''
#     for x in range(16):  # Количество символов (16)
#         pas += random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
#     return pas


def generate_new_password(user: User):
    """Создание нового пароля для существующего пользователя"""
    new_password = User.objects.make_random_password(length=12)
    user.set_password(str(new_password))
    user.save()

    send_mail(
        subject='Востановление пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )

