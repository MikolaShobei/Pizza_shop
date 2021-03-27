from datetime import timedelta

from django.core import mail
from rest_framework_simplejwt.tokens import RefreshToken


class EmailToken(RefreshToken):
    lifetime = timedelta(days=21)


class Utils:
    @staticmethod
    def send_mail(subject, body, to, **kwargs):
        massage = mail.EmailMessage(subject, body, to=to, **kwargs)
        massage.send()

    @staticmethod
    def create_email_token(user):
        return EmailToken().for_user(user).access_token
